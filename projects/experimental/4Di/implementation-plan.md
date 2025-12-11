# 4DI × CuBFF — Phase‑1 Implementation Plan (Execution Roadmap)

**Status:** Planning • v1.0
**Scope:** Build and validate the **ER‑Moat** foundation (provenance‑weighted, entropy‑constrained, distribution‑robust training) with **CuBFF** as an integrity probe.
**Pre‑reads:** 4DI MOC/spec; _Curse of Recursion_; MAD; MMD & DRO; KLIEP/uLSIF; C2PA & watermarking; dedup pipelines; CuBFF/BFF sources.

---

## 0) Phase Objectives & Exit Criteria

**O1.** Establish a **provenance‑first ingestion** that (i) cryptographically records origin (C2PA when present), (ii) statistically detects synthetic text (watermarks + detectors), and (iii) quarantines flagged samples. **Exit:** <1% FPR at target recall on validation suites; auditable logs.

**O2.** Land **web‑scale dedup** (exact + near‑dup) with soft‑dedup weighting. **Exit:** ≥10× drop in exact regurgitation risk vs. baseline (as in prior dedup studies).

**O3.** Train with **density‑ratio weighting + MMD constraint + DRO**; maintain **entropy floors** and **tail‑coverage** targets each round. **Exit:** No statistically significant entropy decline on human dev; tail‑coverage (\hat p_0) under target; stable rare‑token recall.

**O4.** Integrate **CuBFF monitors** as a canary: alarms fire on compressibility spikes/entropy drops consistent with emergent replicator takeover. **Exit:** Detectors trip reliably on CuBFF‑injected low‑entropy sequences.

**O5.** Validate **no‑collapse regime** via **accumulation** (never replace human data across iterations). **Exit:** Error bounded across rounds in line with accumulation results.

---

## 1) Workstreams, Deliverables, Acceptance Tests

### WS‑1 • Provenance & Attribution (D1)

**Deliverables**

- **P1.1**: Ingestion service enforcing **C2PA** parse/verify; fallbacks log missing metadata.
- **P1.2**: **Watermark hypothesis test** (Kirchenbauer et al.) with p‑values per sample. **Decision rule**: reject content if (p \le \alpha\_{\mathrm{wm}}).
- **P1.3**: Auxiliary detectors (**DetectGPT**, **GLTR**) produce a **synthetic posterior** (q\_{\text{syn}}(x)\in[0,1]) used only for weighting/routing, not hard labels.
- **P1.4**: Datasheet template (Gebru et al.) for every corpus shard.

**Acceptance**

- **AUC / power** on watermark+detector blends ≥ target; **FPR** bounded by (\alpha\_{\mathrm{wm}}) on human‑only eval. (Power analysis in §3.1.)

---

### WS‑2 • Dedup & Rare‑Mode Protection (D3)

**Deliverables**

- **D2.1**: Exact‑substring dedup + **SimHash/MinHash** near‑dup (Jaccard/cosine) with cluster metadata.
- **D2.2**: **Soft‑dedup weights** (d(x)\in[0,1]) to reduce, not eliminate, cluster members to preserve tail coverage.

**Acceptance**

- **Regurgitation rate** (nearest‑neighbor string match on held‑out prompts) reduced ≥10× vs. no‑dedup baseline; **type/token diversity** ↑; **Zipf tail** slope stable.

---

### WS‑3 • Distributional Safeguards (D2)

**Deliverables**

- **S3.1**: **KLIEP/uLSIF** density‑ratio estimation to compute (w(x)=p*{\text{human}}(x)/p*{\text{mix}}(x)).
- **S3.2**: Importance‑weighted objective
  [
  \mathcal L*{\text{IW}}(\theta)=\mathbb E*{x\sim D}\big[w(x),d(x),(-\log p_\theta(x))\big].
  ]
- **S3.3**: **MMD** constraint and **entropy floor** (held‑out human dev). Penalize if (\mathrm{MMD}^2!>\tau) or (H(p*\theta)!<H*{\min}).
- **S3.4**: **DRO** (variance‑regularized / (f)-divergence ball) to protect tails:
  [
  \min*\theta\ \sup*{Q:,D*f(Q|\hat P)\le \rho}\ \mathbb E_Q[-\log p*\theta(X)].
  ]

**Acceptance**

- **Two‑sample test** (permutation‑MMD) non‑reject at level (\alpha*{\text{mmd}}) vs. human reference; **entropy** ≥ (H*{\min}); **DRO radius** calibrated (see §3.3) so rare‑token recall does not regress.

---

### WS‑4 • CuBFF Integrity Probes (D4)

**Deliverables**

- **C4.1**: Automated **CuBFF** runs (BFF variants) produce tapes; compute **LZ compression** and **high‑order entropy** curves; maintain archives.
- **C4.2**: **Alarm tests**: when compressibility spikes (replicator takeover), confirm ER‑Moat’s **entropy/MMD sentinels** fire within (k) batches.

**Acceptance**

- Deterministic alarms on positive controls (CuBFF replicators); **no alarms** on human‑only dev.

---

### WS‑5 • Accumulation Protocol (No‑Collapse Regime)

**Deliverables**

- **A5.1**: Data unioning policy: never remove (H) (human reference); record generation (t) for all data.
- **A5.2**: Mixing controller limits **effective synthetic mass** via (w(x)) and quarantine routes.
- **A5.3**: Round‑to‑round dashboard: plot test error vs. (t); verify **bounded** behavior.

**Acceptance**

- **Bounded test error** across ≥3 retrain rounds under accumulation; **no monotone entropy decline** on human dev.

---

## 2) Milestones & Issue Checklist (GitHub‑style)

### M1 • Ingestion & Provenance (WS‑1)

- [ ] C2PA verify/record in metadata store.
- [ ] Watermark detector with calibrated (\alpha\_{\mathrm{wm}}).
- [ ] DetectGPT + GLTR scoring; calibration curves.
- [ ] Datasheets generated per shard.

### M2 • Dedup (WS‑2)

- [ ] Exact + SimHash/MinHash pipelines; cluster logs.
- [ ] Soft‑dedup weighting function (d(x)).

### M3 • ER‑Moat Objective (WS‑3)

- [ ] KLIEP/uLSIF (w(x)) estimation with CV.
- [ ] Add MMD penalty; permutation testing harness.
- [ ] Entropy floor (H\_{\min}) estimator on human dev.
- [ ] DRO solver with (f)-divergence ball.

### M4 • CuBFF Probes (WS‑4)

- [ ] CuBFF runner; entropy/compressibility metrics.
- [ ] Alarm wiring into training sentinels.

### M5 • Accumulation & Rounds (WS‑5)

- [ ] Data‑of‑data ledger; union policy.
- [ ] Round‑over‑round evaluation dashboard.

---

## 3) Statistical Gates & Parameterization (Math)

### 3.1 Watermark Hypothesis Test (Kirchenbauer et al.)

Let (T(x)) be the test statistic (green‑list token bias); define decision rule: **reject** (H*0) (“no watermark”) if (T(x)\ge t*\alpha), where (t*\alpha) is the ((1-\alpha*{\mathrm{wm}})) quantile under the null. **Power target** (\beta) sets **minimum sample length** (n) via standard test‑power analysis for biased token selections—choose (n) so power (1-\beta) at the observed effect size.

### 3.2 Tail‑Coverage Target (Good–Turing)

On each window of size (M), estimate **missing mass** (\hat p*0 \approx n_1/M) with (n_1) singletons. Enforce (\hat p_0 \le \delta) by ensuring **effective real tokens** (M*{\text{real}}=(1-\alpha_s)M \ge n_1/\delta). This sets a **design upper bound** on synthetic fraction (\alpha_s).

### 3.3 MMD Constraint & Thresholding

Compute (\mathrm{MMD}^2) with an RBF kernel on features (\phi(x)). **Threshold (\tau)** via a permutation test: repeatedly shuffle labels between (P*{\text{train}}) and (P*{\text{human}}), compute the null distribution of (\mathrm{MMD}^2), and set (\tau) at the ((1-\alpha\_{\text{mmd}})) quantile.

### 3.4 DRO Radius Calibration

For an (f)-divergence ball around (\hat P) of size (\rho), choose (\rho) using **finite‑sample concentration** (order (O(1/\sqrt{n}))); select (\rho) by CV to balance robustness vs. variance, following Namkoong–Duchi’s convex surrogate.

### 3.5 Entropy Floor

Estimate (H(p*\theta)) on **human‑only dev** via token‑level cross‑entropy; enforce (H(p*\theta)\ge H*{\min}), with (H*{\min}) set to the **lower (95%)** bound of entropy observed on historical (trusted) checkpoints to avoid drift toward low‑entropy equilibria.

---

## 4) Experiment Design (A/B & Ablations)

**Datasets**

- **Human reference (H):** curated, documented with **Datasheets**; provenance recorded (C2PA when available).
- **Mix (D):** post‑filter/post‑dedup pool with per‑sample (q\_{\text{syn}}(x)), (d(x)), and provenance fields.

**Arms**

- **Baseline:** standard ERM on (D) without safeguards.
- **ER‑Moat:** ( \mathcal L*{\text{IW}} + \lambda*{\text{mmd}}\mathrm{MMD}^2 + \mu[H_{\min}-H]\_+^2 + \text{DRO} ).

**Primary Metrics**

- **Held‑out perplexity** on human dev; **entropy** (must not decline).
- **MMD** to human reference (non‑reject at (\alpha\_{\text{mmd}})).
- **Tail coverage** (\hat p_0); **rare‑token recall** measured on a stratified rare‑bin set.
- **Regurgitation** rate (nearest‑neighbor exact match) after prompts.

**Secondary Metrics**

- **Watermark/Detector FPR/FNR** on labeled suites.
- **Zipf tail slope** stability.

**Stopping Rules**

- Halt if entropy drop beyond tolerance; if MMD rejects or (\hat p_0) exceeds (\delta); or if regurgitation increases.

---

## 5) Risk Register & Mitigations

- **R‑1 False positives in synthetic detection.** _Mitigation:_ combine **watermark** (hypothesis test) + **DetectGPT/GLTR**, fuse via calibrated posteriors; gate hard decisions by provenance.
- **R‑2 Over‑pruning rare legitimate content via dedup.** _Mitigation:_ prefer **soft‑dedup**; monitor (\hat p_0) and rare‑token recall; restore cluster exemplars if tail deteriorates.
- **R‑3 Over‑constraint (MMD/DRO) causing underfit.** _Mitigation:_ CV over (\lambda\_{\text{mmd}},\rho); ensure non‑rejection with adequate power.
- **R‑4 Recursive replacement in later rounds.** _Mitigation:_ strict **accumulation protocol**; never remove (H); cap effective synthetic mass via (w(x)).

---

## 6) Engineering Blueprint (Minimal Viable Stack)

- **Data Ledger:** immutable store of ({)hash, source URL/ID, C2PA manifest, detection scores (q\_{\text{syn}}), dedup cluster ID/weight (d(x)), timestamps(}). (C2PA + Datasheets.)
- **Dedup Service:** ExactSubstr + SimHash/MinHash with cluster reports; thresholds in config.
- **Training Orchestrator:** hooks for KLIEP/uLSIF (w(x)); MMD penalty and permutation tester; DRO solver; entropy monitor.
- **CuBFF Runner:** scheduled soups; outputs tapes + entropy/compressibility; feeds sentinel tests.
- **Dashboards:** entropy trend, MMD p‑values, (\hat p_0), regurgitation, watermark FPR/FNR, and round‑over‑round error (accumulation proof).

---

## 7) Phase Timeline (indicative sequencing)

1. **Week 1‑2:** WS‑1 ingestion + watermark/Detectors; Datasheets templates.
2. **Week 2‑3:** WS‑2 dedup service + cluster store.
3. **Week 3‑5:** WS‑3 ER‑Moat objective (KLIEP/uLSIF, MMD, entropy floor, DRO).
4. **Week 4‑6:** WS‑4 CuBFF probes + sentinel wiring.
5. **Week 6‑8:** WS‑5 accumulation rounds; A/B + ablations; dashboards; exit review.

_(Calendar bounds are placeholders for ordering; acceptance criteria remain mathematical/statistical as above.)_

---

## 8) Governance & Documentation

- **Datasheets for every shard** (motivation, composition, collection, preprocessing, curation RACI).
- **Provenance policy**: when C2PA missing, record best‑effort origin; quarantine on detector triggers; manual review pathways.
- **Evaluation cards**: report entropy, MMD, (\hat p_0), regurgitation, and accumulation plots per release.

---

## 9) Direct Ties to Your 4 Directives

- **D1 (Provenance)** → WS‑1, §3.1, §8.
- **D2 (Entropy/Diversity)** → WS‑3, §3.2, §3.3, §3.5.
- **D3 (Rare‑Mode/Dedup)** → WS‑2, §2 acceptance, §4 metrics.
- **D4 (Self‑Replication Governance)** → WS‑4 CuBFF alarms.

---

## 10) References (anchor points used in this plan)

- **Model Collapse / Recursion:** Shumailov et al., 2023.
- **MAD / Accumulation avoids collapse:** Gerstgrasser et al., 2024.
- **MMD (kernel two‑sample):** Gretton et al., 2012.
- **DRO (f‑divergence):** Namkoong & Duchi, 2016.
- **Density‑ratio (KLIEP/uLSIF):** Sugiyama et al., 2007–2008.
- **Entropy & Zipf:** Shannon (1948); Piantadosi (2014 review).
- **Dedup improves LMs / SimHash/MinHash:** Lee et al.; Charikar (2002); Broder (1997).
- **Watermarking / GLTR / DetectGPT:** Kirchenbauer et al., 2023; Gehrmann et al., 2019; Mitchell et al., 2023.
- **C2PA & Datasheets:** Coalition for Content Provenance & Authenticity; Gebru et al., 2018.
- **CuBFF / BFF entropy transitions:** Agüera y Arcas et al., 2024; CuBFF repo.

---

### What this delivers now

- A **concrete, testable plan** tied to your directives and to the literature (no assumptions, no examples).
- **Mathematical gates** (watermark (p)-tests, Good–Turing, MMD permutation tests, DRO radius, entropy floors).
- A **deployment sequence** that proves the **no‑collapse regime** (accumulation + safeguards), with **CuBFF** validating integrity.

If you want, I can split this into:

- `/plans/phase1-implementation.md` (this document)
- `/specs/er-moat.md` (losses, penalties, hyper‑parameters and estimators)
- `/ops/runbooks/ingestion-provenance.md`, `/ops/runbooks/dedup.md`
- `/eval/cards/template.md` (entropy/MMD/tail coverage/regurgitation)

…ready to drop into your repo.
