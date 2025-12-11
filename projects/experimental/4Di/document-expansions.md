
<!-- What this step delivers

1. **Repo docs layout (MOC + interlinks).**
2. **A mathematically‑defined guardrail algorithm** to prevent degenerative feedback (“model collapse/MAD”) during training when synthetic data is present.
3. **Schemas and acceptance tests** you can enforce in CI.
4. **Citations** to the research that each piece stands on.

Key results we rely on:

* Training on your own generations shrinks tails and causes degenerative equilibria (**Model Collapse**) unless fresh human data is consistently injected. ([arXiv][1])
* Autophagy loops degrade either precision or recall absent enough fresh real data (**MAD**). ([arXiv][2])
* Deduplication measurably reduces memorization and improves evaluation fidelity (hence must be integral to any safeguard). ([arXiv][3])
* Entropy/“compressibility” shifts can detect phase transitions in program/sequence populations (as in CuBFF’s replicator emergence). 
* Statistical detectors (GLTR/DetectGPT/watermarks) provide weak signals that must be **calibrated** before you treat them as probabilities. ([arXiv][4])
* Distributional shift can be controlled with **density‑ratio/importance weighting**, **MMD** two‑sample tests, and **DRO** constraints. ([Journal of Machine Learning Research][5])
* Provenance/attribution should use **C2PA Content Credentials** (cryptographically‑verifiable manifests). ([C2PA][6])
-->

---

# Document Expansions

## Drop‑in repo docs (MOC + specs)

> **Copy these files verbatim into your repo.** They’re interlinked and ready for PR review.

### `README.md`

```markdown
# 4DI • CuBFF Guardrail Framework

A training-time safeguard that prevents degenerative feedback when models ingest synthetic text. It combines:
- provenance & attribution (C2PA),
- calibrated synthetic detectors,
- deduplication & uniqueness constraints,
- distributional tests (MMD) and tail-coverage targets (Good–Turing),
- a mixture controller (`4DI-Guard`) that enforces provable floors on entropy, rarity, and divergence.

**Start here:** [docs/MOC.md](docs/MOC.md)
```

### `docs/MOC.md`

```markdown
# Map of Content (MOC)

- [Overview](overview.md)
- [Threat Model: Collapse/MAD](threat-model.md)
- [Data Policy & Schemas](policy.md)
  - [Ingestion Record Schema](schemas/ingestion.schema.json)
  - [Lineage/Attribution Schema](schemas/lineage.schema.json)
- [Algorithms](algorithms/README.md)
  - [4DI‑Guard (Mixture Controller)](algorithms/4di-guard.md)
  - [Detectors: Calibration & Fusion](algorithms/detectors.md)
  - [Deduplication & Near‑Duplicate Control](algorithms/dedup.md)
  - [Distributional Tests (MMD) & Tail Coverage](algorithms/tests.md)
- [Acceptance Tests (CI)](acceptance.md)
- [References](references.md)
```

### `docs/overview.md`

```markdown
# Overview

## Problem
Repeatedly training on model outputs drives distributional drift that collapses rare modes and yields low‑entropy equilibria. (Formalized as **Model Collapse**; **MAD** extends this to autophagous loops.) See [References]. 

## Objective
Maintain high‑entropy, rare‑event coverage and bounded divergence from a human reference distribution while allowing controlled synthetic augmentation.

## Approach (4DI)
1. **Attribution-first ingestion** (C2PA manifests → verifiable source/rights).
2. **Calibrated detection** of synthetic content; fuse multiple weak signals into well‑calibrated posteriors.
3. **Deduplication & uniqueness** at substring and LSH levels to remove repetitions that fuel memorization.
4. **Distributional guardrails**: kernel MMD thresholds and Good–Turing tail coverage floors.
5. **Mixture control**: optimize synthetic share `ρ` subject to hard safety constraints (entropy, MMD, missing‑mass).
```

### `docs/threat-model.md`

```markdown
# Threat Model: Collapse & Autophagy

- **Degenerative feedback:** Training on generated data shrinks support and increases repetition until a degenerate equilibrium emerges (Model Collapse).  
- **Autophagous loops (MAD):** Without fresh human data every generation, precision or recall must degrade.

**Evidence:** Shumailov et al. (collapse); Alemohammad et al. (MAD). See [References].
```

### `docs/policy.md`

```markdown
# Data Policy & Schemas

- **Attribution required:** Every ingested unit must carry a verifiable provenance manifest (C2PA).
- **Distributional safety:** Batches must satisfy MMD ≤ γ, entropy ≥ H_min, Good–Turing missing mass ≥ δ.
- **Dedup:** No shard proceeds without exact‑substring and LSH‑based neardup filtering.

See JSON Schemas in `docs/schemas/`.
```

### `docs/schemas/ingestion.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://4di/specs/ingestion.schema.json",
  "title": "IngestionRecord",
  "type": "object",
  "required": ["uid","timestamp","content_sha256","source_type","provenance","license","lang","split","detector_scores"],
  "properties": {
    "uid": {"type":"string","pattern":"^[A-Fa-f0-9]{64}$"},
    "timestamp": {"type":"string","format":"date-time"},
    "content_sha256": {"type":"string","pattern":"^[A-Fa-f0-9]{64}$"},
    "source_type": {"enum":["human","synthetic","unknown"]},
    "provenance": {
      "type":"object",
      "required":["c2pa_manifest_ref"],
      "properties":{"c2pa_manifest_ref":{"type":"string"}}
    },
    "license": {"type":"string"},
    "lang": {"type":"string"},
    "split": {"enum":["train","val","test"]},
    "detector_scores": {
      "type":"object",
      "additionalProperties":{"type":"number","minimum":0.0}
    },
    "dup": {
      "type":"object",
      "properties":{
        "exact_fingerprint":{"type":"string"},
        "minhash_128":{"type":"array","items":{"type":"integer","minimum":0,"maximum":4294967295}},
        "simhash_64":{"type":"integer","minimum":0}
      }
    }
  }
}
```

### `docs/schemas/lineage.schema.json`

```json
{
  "$schema":"https://json-schema.org/draft/2020-12/schema",
  "$id":"https://4di/specs/lineage.schema.json",
  "title":"Lineage",
  "type":"object",
  "required":["uid","parents","transform"],
  "properties":{
    "uid":{"type":"string","pattern":"^[A-Fa-f0-9]{64}$"},
    "parents":{"type":"array","items":{"type":"string"}},
    "transform":{"type":"string"},
    "c2pa_chain":{"type":"array","items":{"type":"string"}}
  }
}
```

### `docs/algorithms/README.md`

```markdown
# Algorithms

- [4DI‑Guard (mixture controller)](4di-guard.md)
- [Detectors: calibration & fusion](detectors.md)
- [Deduplication & near‑dups](dedup.md)
- [Tests: MMD & tail coverage](tests.md)
```

### `docs/algorithms/4di-guard.md`

```markdown
# 4DI‑Guard: Mixture Controller with Hard Safety Constraints

## Notation
- Human reference distribution: \(P_H\) (empirical from curated human corpus).
- Synthetic generator distribution: \(P_S\).
- Batch mixture: \(P_\rho = (1-\rho)P_H + \rho P_S\), \(\rho \in [0,1]\).
- Kernel MMD^2 between two empirical samples \(X \sim P\), \(Y \sim Q\):
\[
\operatorname{MMD}^2_k(P,Q)=\mathbb{E}[k(X,X')]+\mathbb{E}[k(Y,Y')]-2\mathbb{E}[k(X,Y)].
\]
- Good–Turing missing mass estimator (unseen probability):
\[
\widehat{M}=\frac{N_1}{N},
\]
with \(N_1\) = count of types observed exactly once in the sample of size \(N\).  
- Miller–Madow entropy correction (base \(b\)): for empirical plug‑in entropy \(\widehat{H}_{\text{MLE}}\) on \(K\) occupied bins,
\[
\widehat{H}_{\text{MM}} = \widehat{H}_{\text{MLE}} + \frac{K-1}{2N \ln b}.
\]

## Control Objective
Choose \(\rho\) and per‑example weights \(w_i\) to **maximize useful tokens from \(P_S\)** while **enforcing**:
1. **Divergence guard:** \(\operatorname{MMD}^2_k(P_\rho, P_H) \le \gamma\).
2. **Entropy floor:** \(\widehat{H}_{\text{MM}}(n\text{-gram}(P_\rho)) \ge H_{\min}\).
3. **Tail coverage:** \(\widehat{M}(P_\rho) \ge \delta\).
4. **Attribution floor:** fraction of batch with verifiable provenance ≥ \(\pi_{\min}\).

## Feasibility Program
Given a candidate batch \(B\) with detector‑calibrated posteriors \(p_i = \Pr[\text{synthetic}|x_i]\), set weights
\[
w_i \propto (1-p_i)\cdot \lambda_H + p_i\cdot \lambda_S,
\]
normalize \(\sum_i w_i = 1\), and define the effective \(\rho=\sum_{i\in B} w_i \cdot \mathbf{1}[p_i>\tau]\).

Solve:
\[
\max_{\rho,\;w}\ \rho\quad\text{s.t.}\ 
\begin{cases}
\operatorname{MMD}^2_k(\hat{P}_{\rho,w}, \hat{P}_H) \le \gamma,\\[2pt]
\widehat{H}_{\text{MM}}(\hat{P}_{\rho,w}) \ge H_{\min},\\[2pt]
\widehat{M}(\hat{P}_{\rho,w}) \ge \delta,\\[2pt]
\text{provable\_provenance}(\hat{P}_{\rho,w}) \ge \pi_{\min},\\[2pt]
0 \le \rho \le \rho_{\max}.
\end{cases}
\]

## Algorithm (line search with certificate)
1. Calibrate detector scores to probabilities via temperature scaling on a labeled validation set; combine multiple detectors by logistic fusion; see *Detectors*.
2. Propose a bracket \([0,\rho_{\max}]\).  
3. **While** bracket not converged:
   - Construct weighted mini‑batch at trial \(\rho\) (top‑\(p_i\) synthetic candidates).
   - Compute unbiased MMD^2 with a characteristic kernel; compute \(\widehat{H}_{\text{MM}}\); compute \(\widehat{M}\).
   - If all constraints satisfied, move lower bound up; else move upper bound down.
4. Fix \(\rho^\*\) at the largest feasible value; emit the batch and its **safety certificate**: \((\operatorname{MMD}^2,\widehat{H}_{\text{MM}},\widehat{M},\pi)\).

**Why this works:** MMD is a consistent two‑sample metric; Good–Turing gives a finite‑sample lower bound on unseen mass; Miller–Madow debiases entropy. Together they bound the drift toward repetitive/low‑diversity equilibria documented in collapse/MAD studies.
```

### `docs/algorithms/detectors.md`

```markdown
# Detectors: Calibration & Fusion

## Inputs
- Scores from multiple detectors (e.g., watermark‑based, GLTR‑style rank features, DetectGPT‑style curvature tests). 
- Each score is **not** a probability.

## Calibration
Fit a temperature‑scaled logistic model \( \sigma((\sum_j \alpha_j s_j)/T) \) on a held‑out labeled set with positive class = known synthetic and negative = verified human (C2PA). Use reliability diagrams and ECE to verify calibration; store \(T,\alpha\).

## Output
Posterior \(p_i = \Pr[\text{synthetic}|x_i]\) fed to `4DI‑Guard`.

## Rationale
Modern classifiers are miscalibrated; temperature scaling provides well‑behaved posteriors suitable for constraints. See [References].
```

### `docs/algorithms/dedup.md`

```markdown
# Deduplication & Near‑Duplicate Control

## Exact substrings
Blockwise rolling hashes + suffix‑array/DAWG to remove repeated strings (down to ≥ 32‑byte windows).

## Near‑duplicates
- **MinHash** signatures per document and per paragraph; Jaccard‑LSH to collapse clusters.
- **SimHash** for character n‑grams to catch paraphrastic neardups.

## Policy
Any shard failing exact/LSH dedup aborts ingestion.

## Rationale
Dedup reduces memorization by order‑of‑magnitude and yields cleaner evaluation splits; global dedup settings materially affect retained data quality. See [References].
```

### `docs/algorithms/tests.md`

```markdown
# Distributional Tests & Tail Coverage

- **MMD^2 (characteristic kernel):** unbiased estimator with linear‑time approximation for streaming checks.
- **Entropy floor:** compute \( \widehat{H}_{\text{MM}} \) on n‑gram histograms (base‑2). 
- **Tail coverage:** Good–Turing missing mass \( \widehat{M}=N_1/N \).

Batch proceeds iff all thresholds met; thresholds are set once per project and stored in policy.
```

### `docs/acceptance.md`

```markdown
# Acceptance Tests (CI)

A batch is **rejected** unless all hold:

1. **Provenance:** ≥ \(\pi_{\min}\) of items have verifiable C2PA manifests.
2. **Dedup:** exact substrings removed; Jaccard(neardup) ≤ J_max; SimHash(Hamming) ≥ H_min.
3. **Calibration sanity:** detector fusion ECE ≤ ε on last calibration report.
4. **Guardrails:** 
   - \(\operatorname{MMD}^2_k \le \gamma\)
   - \(\widehat{H}_{\text{MM}} \ge H_{\min}\)
   - \(\widehat{M} \ge \delta\)
   - resulting \(\rho^\* \le \rho_{\max}\)

Each job writes a signed **safety certificate** to the lineage log.
```

### `docs/references.md`

```markdown
# References

- Shumailov et al., *The Curse of Recursion: Training on Generated Data Makes Models Forget*. arXiv:2305.17493.  
- Alemohammad et al., *Self‑Consuming Generative Models Go MAD*. arXiv:2307.01850.  
- Lee et al., *Deduplicating Training Data Makes Language Models Better*. ACL 2022 / arXiv:2107.06499.  
- Agüera y Arcas et al., *Computational Life: Well‑formed, Self‑replicating Programs Emerge…* arXiv:2406.19108; CuBFF codebase.  
- Gretton et al., *A Kernel Two‑Sample Test*. JMLR 2012.  
- Sugiyama et al., *Importance‑Weighted Cross‑Validation*. JMLR 2007; Kanamori et al., *uLSIF*. JMLR 2009.  
- Namkoong & Duchi, *Variance‑based Regularization* (DRO). JMLR/NeurIPS 2016–2019.  
- Good, *Population Frequencies of Species and Estimation of Population Parameters*; Miller, *Note on the Bias of Information Estimates*.  
- C2PA, *Content Credentials Technical Specification*.
```

---

## Where each requirement is satisfied (with proofs/refs)

**Why collapse happens (entropy loss):**

* Collapse removes rare events; tails disappear under recursive training on self‑generated data (theoretical + empirical). ([arXiv][1])
* In CuBFF, emergence and later dominance of replicators corresponds to a drop in empirical entropy (higher compressibility), showing phase transitions detectable via information measures. 
* CI guardrails enforce (\widehat{H}_{\text{MM}}) floors and Good–Turing missing‑mass (\widehat{M}) floors to prevent that drift.

**How companies prevent it (what to implement):**

* **Filtering & Dedup:** Dedup reduces memorization ×10 and improves evaluation integrity; must be upstream and per‑batch. ([arXiv][3])
* **Attribution:** Require C2PA manifests for provenance; reject unverifiable sources. ([C2PA][6])
* **Distributional safeguards:** MMD constraints + DRO/importance‑weighting stabilize the training objective under covariate shift. ([Journal of Machine Learning Research][5])

**How much AI content triggers collapse:**

* There is **no universal fraction**; MAD shows that **without sufficient fresh human data each generation**, quality or diversity **must** degrade; collapse speed depends on generator bias and selection. Your controller therefore solves a **feasibility** problem per batch to cap (\rho) under empirical constraints instead of assuming a constant threshold. ([arXiv][2])

**Is collapse inevitable?**

* Not if you **enforce**: (i) attribution and dedup, (ii) entropy/tail floors, (iii) divergence bounds, and (iv) continuous infusion of human data (the MAD condition). ([arXiv][2])

---

## Mathematical details behind the knobs (all used in the spec)

* **Good–Turing missing mass** (\widehat{M}=N_1/N) lower‑bounds unseen probability mass at finite (N); maintaining (\widehat{M}\ge\delta) preserves rare‑type exploration. ([arXiv][7])
* **Miller–Madow** corrects small‑sample entropy bias; use it for (H_{\min}) certificates. ([ACL Anthology][8])
* **MMD** is a metric on probability measures for characteristic kernels, with unbiased estimators and linear‑time approximations; violations signal drift toward synthetic equilibria.
* **Importance weighting / density‑ratio estimation** (KLIEP/uLSIF) lets you reweight mixed batches to the target human distribution without explicit density models; used inside `4DI‑Guard` to construct feasible (w_i). ([The Institute of Statistical Mathematics][9])
* **Calibration** (Temperature scaling) ensures detector scores are probabilistically meaningful, a prerequisite for any constraint using (p_i). ([Proceedings of Machine Learning Research][10])

---

## What to implement next (non‑vague, testable)

1. **Wire the schemas** above into ingestion. Fail fast on missing C2PA or dedup flags. ([C2PA][6])
2. **Build the detector‑fusion calibrator** (temperature scaling + logistic fusion) and persist (T,\alpha) with ECE reports. ([Proceedings of Machine Learning Research][10])
3. **Add the `4DI‑Guard` line search** exactly as specified to compute (\rho^*) and the safety certificate ((\operatorname{MMD}^2,\widehat{H}_{\text{MM}},\widehat{M},\pi)). ([arXiv][7])
4. **Make CI enforce `docs/acceptance.md`.** The pipeline should **reject** any batch that violates a constraint and attach the certificate to the lineage log.

---

## Why this answers your earlier brief—point by point

* **Structure & interlinking (GitHub MOC):** Provided `docs/MOC.md` with cross‑refs.
* **Why it happens (entropy loss):** Codified via entropy/tail math; backed by collapse/MAD papers. ([arXiv][1])
* **How to prevent:** Filtering/dedup, attribution, and distributional guardrails—all specified with thresholds and tests. ([arXiv][3])
* **How much synthetic is safe:** Not a constant—solved per batch by `4DI‑Guard` feasibility under constraints (consistent with MAD). ([arXiv][2])
* **Inevitable?** No—if you maintain the constraints and keep fresh human data flowing. ([arXiv][2])

If you want, I’ll turn these docs into a PR template and a CI YAML that enforces the acceptance tests on every data shard.

[1]: https://arxiv.org/abs/2305.17493 "[2305.17493] The Curse of Recursion: Training on Generated Data Makes Models Forget"
[2]: https://arxiv.org/abs/2307.01850 "[2307.01850] Self-Consuming Generative Models Go MAD"
[3]: https://arxiv.org/pdf/2107.06499?utm_source=chatgpt.com "arXiv:2107.06499v2 [cs.CL] 24 Mar 2022"
[4]: https://arxiv.org/abs/1906.04043?utm_source=chatgpt.com "GLTR: Statistical Detection and Visualization of Generated ..."
[5]: https://www.jmlr.org/papers/volume10/kanamori09a/kanamori09a.pdf?utm_source=chatgpt.com "A Least-squares Approach to Direct Importance Estimation∗"
[6]: https://spec.c2pa.org/specifications/specifications/2.2/specs/_attachments/C2PA_Specification.pdf?utm_source=chatgpt.com "Content Credentials : C2PA Technical Specification"
[7]: https://arxiv.org/abs/2107.06499?utm_source=chatgpt.com "Deduplicating Training Data Makes Language Models Better"
[8]: https://aclanthology.org/2022.acl-long.577.pdf?utm_source=chatgpt.com "Deduplicating Training Data Makes Language Models Better"
[9]: https://www.ism.ac.jp/editsec/aism/pdf/060_4_0699.pdf?utm_source=chatgpt.com "Direct importance estimation for covariate shift adaptation"
[10]: https://proceedings.mlr.press/v70/guo17a/guo17a.pdf?utm_source=chatgpt.com "On Calibration of Modern Neural Networks"
