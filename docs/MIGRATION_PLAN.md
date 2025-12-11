# UDL Monorepo Migration Plan

## Current Status Assessment

### Repositories Needing Attention

**Uncommitted Changes (14 repos):**

- axe_syntax (2 files)
- black-milk (4 files)
- camo-obsidian (1 file)
- canon (1 file)
- CLAY (1 file)
- ctx-card (4 files)
- DrRx (1 file)
- FINK (1 file)
- gate (2 files)
- hoc (1 file)
- mecha_development (1 file)
- milkDocs (1 file)
- motleyBard (4 files)
- PACER (1 file)
- remedysyntax (1 file)
- robo_md (8 files)

**Unpushed Commits (5 repos):**

- canon (1 commit)
- CLAY (4 commits)
- DrRx (1 commit)
- FINK (2 commits)
- milkDocs (2 commits)
- PACER (1 commit)

**Not Git Repos (5 directories):**

- 1az
- axe-Syntax
- gateppattern-1.1
- mecha_lang
- udl-directory-template

## Migration Strategy Decision

### Recommended: TurboRepo + Git Subtree

**Pros:**

- Preserves full git history for all projects
- Language-agnostic (supports Python, TypeScript, Rust, GDScript)
- Intelligent caching and parallel execution
- Easy to understand and maintain
- Can split repos back out if needed

**Implementation Timeline:** 2-3 days

## Step-by-Step Migration Plan

### Phase 0: Preparation (30 minutes)

**Step 0.1: Backup Everything**

```bash
cd /Users/deadcoast/github
tar -czf UDL-backup-$(date +%Y%m%d).tar.gz UDL/
```

**Step 0.2: Clean Up Uncommitted Changes**

For each repo with uncommitted changes, decide:

- Commit them? (recommended)
- Stash them?
- Discard them? (careful!)

**Step 0.3: Push All Commits**

Push all unpushed commits to GitHub.

**Step 0.4: Initialize Non-Git Directories**

For 1az, axe-Syntax, gateppattern-1.1, mecha_lang:

- Initialize git
- Add remote
- Push to GitHub

### Phase 1: Initialize Monorepo Structure (1 hour)

**Step 1.1: Initialize UDL as Git Repo**

```bash
cd /Users/deadcoast/github/UDL
git init
git checkout -b main
```

**Step 1.2: Create Directory Structure**

```bash
mkdir -p .github/workflows
mkdir -p tooling/{scripts,templates,dev-tools}
mkdir -p docs/{projects,specs}
mkdir -p shared/{configs,packages,assets}
mkdir -p projects/{languages,tools,extensions,applications,libraries,experimental}
mkdir -p examples
mkdir -p .archive
```

**Step 1.3: Create Core Configuration Files**

Create:

- `package.json` (root)
- `pnpm-workspace.yaml`
- `turbo.json`
- `Cargo.toml` (workspace)
- `.gitignore`
- `.gitattributes`
- `README.md`

**Step 1.4: Initial Commit**

```bash
git add .
git commit -m "feat: initialize UDL monorepo structure"
```

### Phase 2: Set Up Package Managers (30 minutes)

**Step 2.1: Set Up PNPM Workspace**

```bash
npm install -g pnpm
pnpm init
```

**Step 2.2: Set Up Python Workspace**

Install poetry or use pip + pyproject.toml

**Step 2.3: Set Up Rust Workspace**

Configure Cargo.toml workspace section

**Step 2.4: Install TurboRepo**

```bash
pnpm add -Dw turbo
```

### Phase 3: Migrate Projects (2-4 hours)

**Strategy A: Preserve History (Recommended but Slower)**

For each project:

```bash
# Example: axe-syntax
git remote add axe-syntax-origin https://github.com/deadcoast/axe-syntax.git
git subtree add --prefix=projects/tools/axe-syntax axe-syntax-origin main
```

**Strategy B: Fresh Start (Faster but Loses History)**

For each project:

```bash
# Move directory
mv axe-Syntax projects/languages/axe-syntax

# Copy over git history if desired
cp -r axe-Syntax/.git projects/languages/axe-syntax/.git-history
```

**Strategy C: Hybrid (Recommended for this case)**

Use subtree for important projects, fresh start for experimental/small ones.

### Phase 4: Configure Projects (1-2 hours)

**Step 4.1: Add project.json to Each Project**

**Step 4.2: Update package.json/pyproject.toml**

Add workspace references.

**Step 4.3: Update Import Paths**

Update any internal dependencies.

### Phase 5: Set Up CI/CD (1 hour)

**Step 5.1: Create GitHub Workflows**

- `.github/workflows/ci-python.yml`
- `.github/workflows/ci-typescript.yml`
- `.github/workflows/ci-rust.yml`

**Step 5.2: Configure TurboRepo**

Update `turbo.json` with pipeline configuration.

**Step 5.3: Test CI Locally**

```bash
turbo run build
turbo run test
```

### Phase 6: Documentation (1 hour)

**Step 6.1: Generate Project Index**

**Step 6.2: Update Individual READMEs**

Add monorepo context to each project README.

**Step 6.3: Update Root README**

**Step 6.4: Verify CLAUDE.md**

Already done! ✓

### Phase 7: Push to GitHub (15 minutes)

**Step 7.1: Create GitHub Repository**

```bash
gh repo create deadcoast/UDL --public --source=. --remote=origin
```

**Step 7.2: Push**

```bash
git push -u origin main
```

**Step 7.3: Archive Old Repositories**

Add deprecation notices to old individual repos.

### Phase 8: Validation (30 minutes)

**Step 8.1: Clone Fresh Copy**

```bash
cd /tmp
git clone https://github.com/deadcoast/UDL.git
cd UDL
```

**Step 8.2: Run Bootstrap**

```bash
./tooling/scripts/bootstrap.sh
```

**Step 8.3: Test Builds**

```bash
turbo run build
turbo run test
```

**Step 8.4: Smoke Test Each Project**

## Quick Start Option: Minimal Viable Monorepo

If you want to get started quickly without all the fancy tooling:

### Minimal Setup (30 minutes)

```bash
# 1. Init git
cd /Users/deadcoast/github/UDL
git init
git checkout -b main

# 2. Create basic structure
mkdir -p projects/{languages,tools,apps}
mkdir -p docs shared .archive

# 3. Move projects (keeping .git directories)
mv axe-Syntax projects/languages/
mv CTX projects/tools/
mv sandbag projects/tools/
mv black-milk projects/apps/
# ... etc

# 4. Create simple .gitignore
cat > .gitignore << 'EOF'
**/node_modules
**/.venv
**/venv
**/target
**/.pytest_cache
**/__pycache__
**/.DS_Store
**/dist
**/build
**/*.pyc
EOF

# 5. Commit
git add .
git commit -m "feat: migrate to monorepo structure"

# 6. Push
gh repo create deadcoast/UDL --public --source=. --remote=origin
git push -u origin main
```

Then gradually add tooling later.

## Rollback Plan

If something goes wrong:

**Option 1: Restore from Backup**

```bash
cd /Users/deadcoast/github
rm -rf UDL
tar -xzf UDL-backup-YYYYMMDD.tar.gz
```

**Option 2: Keep Old Repos Intact**

Don't delete old GitHub repos until monorepo is proven stable.

**Option 3: Git Subtree Split**

Can split projects back out if needed:

```bash
git subtree split -P projects/tools/sandbag -b sandbag-split
```

## Decision Points

### 1. Full Migration vs Minimal Start?

- **Full Migration**: Complete setup with TurboRepo, workspaces, CI/CD
  - Pro: Everything works immediately
  - Con: 1-2 days of work

- **Minimal Start**: Basic git monorepo, add tooling later
  - Pro: Done in 30 minutes
  - Con: No advanced features initially

### 2. History Preservation?

- **Preserve All History**: Use git subtree
  - Pro: Complete audit trail
  - Con: Complex merge history

- **Fresh Start**: Move directories, archive history
  - Pro: Clean, simple
  - Con: Lose commit history in main repo

### 3. Project Organization?

- **By Category**: /languages, /tools, /apps (Recommended)
- **By Language**: /python, /typescript, /rust
- **Flat**: All projects in /projects

## Recommended Approach for You

Based on your setup, I recommend:

**Phase 1 (Today - 1 hour):**

1. Commit and push all changes ✓
2. Back up everything ✓
3. Minimal monorepo setup
4. Push to GitHub

**Phase 2 (This Week):**

1. Add TurboRepo
2. Set up workspaces
3. Configure CI/CD

**Phase 3 (Next Week):**

1. Add shared packages
2. Create tooling scripts
3. Document everything

This gives you immediate benefits while allowing incremental improvement.

## Next Action

What would you like to do first?

A. Clean up uncommitted changes and push everything
B. Start minimal monorepo setup (30 min)
C. Go for full migration with TurboRepo (1-2 days)
D. Review and customize the architecture first
