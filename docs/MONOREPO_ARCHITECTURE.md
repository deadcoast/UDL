# UDL Monorepo Architecture

## Philosophy

**"Unified by Convention, Independent by Design"**

This monorepo embraces polyglot development while providing unified tooling, CI/CD, and documentation. Each project maintains its independence while benefiting from shared infrastructure.

## Directory Structure

```
UDL/
├── .github/
│   ├── workflows/                 # Centralized CI/CD
│   │   ├── ci-python.yml         # Python project CI
│   │   ├── ci-typescript.yml     # TypeScript project CI
│   │   ├── ci-rust.yml           # Rust project CI
│   │   ├── ci-godot.yml          # Godot project CI
│   │   └── release.yml           # Automated releases
│   └── CODEOWNERS                # Project ownership
│
├── tooling/
│   ├── scripts/
│   │   ├── bootstrap.sh          # Setup script for new devs
│   │   ├── check-changes.sh      # Detect changed projects
│   │   ├── run-in-project.sh     # Execute command in project
│   │   └── sync-deps.sh          # Sync shared dependencies
│   ├── templates/                # Project templates
│   │   ├── python-project/
│   │   ├── typescript-project/
│   │   ├── rust-project/
│   │   └── godot-project/
│   └── dev-tools/
│       ├── monorepo-cli/         # Custom CLI for repo management
│       └── generators/           # Code generators
│
├── docs/
│   ├── CLAUDE.md                 # AI assistant guide (✓ exists)
│   ├── CONTRIBUTING.md           # Contribution guidelines
│   ├── ARCHITECTURE.md           # Overall architecture
│   ├── MIGRATION_GUIDE.md        # Migration from independent repos
│   ├── projects/                 # Per-project docs index
│   └── specs/                    # Shared specifications
│       ├── CTX-CARD-SPEC.md
│       ├── DSL-PATTERNS.md
│       └── TESTING-STANDARDS.md
│
├── shared/
│   ├── configs/                  # Shared configs
│   │   ├── .prettierrc.json
│   │   ├── .eslintrc.json
│   │   ├── pyproject.toml        # Base Python config
│   │   ├── rust-clippy.toml
│   │   └── tsconfig.base.json
│   ├── packages/                 # Shared code libraries
│   │   ├── ctx-common/           # CTX-CARD utilities (Python)
│   │   ├── dsl-toolkit/          # DSL parsing utilities (TS)
│   │   ├── udl-testing/          # Testing utilities
│   │   └── ast-helpers/          # AST manipulation helpers
│   └── assets/                   # Shared assets
│       └── branding/
│
├── projects/
│   ├── languages/                # DSL implementations
│   │   ├── axe-syntax/
│   │   ├── gate/
│   │   ├── f8syntax/
│   │   ├── 1az/
│   │   └── drrx/
│   ├── tools/                    # Developer tools
│   │   ├── ctx/
│   │   ├── sandbag/
│   │   ├── axe/
│   │   └── ctx-card/
│   ├── extensions/               # Editor extensions
│   │   ├── camo-obsidian/
│   │   ├── remedy-syntax/
│   │   └── vscode-udl/
│   ├── applications/             # Full applications
│   │   ├── black-milk/
│   │   ├── strawberrymause/
│   │   └── ascii-string-ui-editor/
│   ├── libraries/                # Reusable libraries
│   │   ├── jetson/
│   │   ├── barrelman/
│   │   └── hunt-ascii/
│   └── experimental/             # WIP/Research projects
│       ├── mecha-lang/
│       ├── motley-bard/
│       └── robo-md/
│
├── examples/                     # Cross-project examples
│   ├── ctx-integration/
│   ├── multi-language-dsl/
│   └── full-stack-udl/
│
├── .archive/                     # Deprecated/archived projects
│   └── depreciated/              # Move existing .depreciated here
│
├── pnpm-workspace.yaml           # PNPM workspace config
├── turbo.json                    # TurboRepo configuration
├── Cargo.toml                    # Rust workspace
├── pyproject.toml                # Python workspace (PEP 660)
├── package.json                  # Root package.json
├── .gitignore
├── .gitattributes
├── README.md
└── CLAUDE.md                     # ✓ Already exists
```

## Technology Stack

### Monorepo Orchestration

**Option 1: TurboRepo (Recommended)**

- Best for polyglot repos
- Intelligent caching and parallelization
- Language-agnostic
- Incremental builds

**Option 2: Nx**

- More features but more complex
- Strong TypeScript integration
- Better for large-scale

**Option 3: Custom (Lightweight)**

- Bash scripts + Make
- No external dependencies
- Full control

### Package Management

- **JavaScript/TypeScript**: PNPM (faster than npm/yarn, better monorepo support)
- **Python**: Poetry with workspace support OR pip + pyproject.toml
- **Rust**: Cargo workspaces (built-in)
- **Godot**: Custom scripts (no package manager)

### CI/CD Strategy

```yaml
# Smart CI that only tests changed projects
name: CI

on: [push, pull_request]

jobs:
  detect-changes:
    runs-on: ubuntu-latest
    outputs:
      python: ${{ steps.filter.outputs.python }}
      typescript: ${{ steps.filter.outputs.typescript }}
      rust: ${{ steps.filter.outputs.rust }}
    steps:
      - uses: actions/checkout@v3
      - uses: dorny/paths-filter@v2
        id: filter
        with:
          filters: |
            python:
              - 'projects/**/*.py'
              - 'shared/packages/**/*.py'
            typescript:
              - 'projects/**/*.ts'
              - 'shared/packages/**/*.ts'
            rust:
              - 'projects/**/*.rs'
              - 'Cargo.toml'

  test-python:
    needs: detect-changes
    if: needs.detect-changes.outputs.python == 'true'
    runs-on: ubuntu-latest
    # ... Python test jobs

  test-typescript:
    needs: detect-changes
    if: needs.detect-changes.outputs.typescript == 'true'
    runs-on: ubuntu-latest
    # ... TypeScript test jobs
```

## Project Metadata Standard

Each project has a `project.json` manifest:

```json
{
  "name": "axe-syntax",
  "version": "0.1.0",
  "type": "tool",
  "category": "languages",
  "language": "python",
  "status": "stable",
  "maintainers": ["@deadcoast"],
  "dependencies": {
    "internal": ["ctx-common"],
    "external": ["textual", "loguru"]
  },
  "scripts": {
    "dev": "python -m axe_syntax",
    "test": "pytest",
    "build": "python -m build",
    "publish": "python -m twine upload dist/*"
  },
  "outputs": {
    "cli": "axe",
    "package": "axe-syntax"
  },
  "docs": "./README.md",
  "github": "https://github.com/deadcoast/axe-syntax"
}
```

## Migration Strategy

### Phase 1: Preserve History ✨

**Keep Git History Using Subtree Strategy:**

```bash
# For each project, we'll preserve full git history
# Example for axe-syntax:

git subtree add --prefix=projects/languages/axe-syntax \
  https://github.com/deadcoast/axe-syntax.git main

# This preserves ALL commit history
```

**Alternative: Git Submodules** (less recommended)

- Keeps repos separate
- More complex workflow
- Good for truly independent evolution

### Phase 2: Restructure

1. Create new monorepo structure
2. Move projects to categorized directories
3. Add project.json manifests
4. Set up shared tooling
5. Configure workspace package managers

### Phase 3: Tooling

1. Set up TurboRepo/Nx
2. Configure CI/CD pipelines
3. Create bootstrap scripts
4. Set up pre-commit hooks
5. Configure automated releases

### Phase 4: Documentation

1. Generate project index
2. Create cross-project guides
3. Set up API documentation
4. Document internal dependencies

## Versioning Strategy

**Semantic Versioning with Independent Releases:**

- Each project has its own version
- Monorepo itself has a version (for tooling)
- Use Changesets or Lerna for coordinated releases
- Tags: `axe-syntax@v1.0.0`, `ctx@v2.1.0`

## Development Workflow

### Initial Setup

```bash
# Clone monorepo
git clone https://github.com/deadcoast/UDL.git
cd UDL

# Run bootstrap script
./tooling/scripts/bootstrap.sh

# This will:
# - Install all language toolchains
# - Set up PNPM/Poetry/Cargo workspaces
# - Install pre-commit hooks
# - Configure git
```

### Working on a Project

```bash
# Navigate to project
cd projects/tools/sandbag

# Install dependencies (automatic from root)
# No need to run separate commands

# Run project-specific commands
cargo build
cargo test

# Or use monorepo CLI
udl run sandbag build
udl test sandbag
```

### Adding Dependencies

```bash
# Internal dependency
udl add-dep sandbag --internal ctx-common

# External dependency
udl add-dep sandbag --external clap@4.0
```

### Creating a New Project

```bash
udl create --name my-dsl --type language --lang typescript
# Generates from template
```

## Cross-Project Dependencies

**Internal Package References:**

```json
// TypeScript (package.json)
{
  "dependencies": {
    "@udl/dsl-toolkit": "workspace:*",
    "@udl/ctx-common": "workspace:*"
  }
}
```

```toml
# Python (pyproject.toml)
[tool.poetry.dependencies]
udl-ctx-common = { path = "../../../shared/packages/ctx-common", develop = true }
```

```toml
# Rust (Cargo.toml)
[dependencies]
udl-ast-helpers = { path = "../../../shared/packages/ast-helpers" }
```

## Testing Strategy

### Levels

1. **Unit Tests**: Per-project
2. **Integration Tests**: Cross-project in `/examples`
3. **E2E Tests**: Full workflows
4. **Performance Tests**: Benchmarks in each project

### Execution

```bash
# Test everything (slow)
turbo run test

# Test only changed projects (fast)
turbo run test --filter=[HEAD^1]

# Test specific project
turbo run test --filter=sandbag

# Test project + dependents
turbo run test --filter=ctx-common...
```

## Documentation Strategy

### Auto-Generated Index

```bash
# Generate project list
udl docs generate-index

# Creates docs/PROJECT_INDEX.md with:
# - All projects
# - Status, category, language
# - Quick links
# - Dependency graph
```

### Cross-References

Use standardized format: `[project:sandbag]`, `[spec:CTX-CARD]`

Tools auto-link these in markdown.

## Release Strategy

### Automated Releases

```bash
# Create changeset
udl changeset

# Example output:
# Which projects changed? (space to select)
# ◯ sandbag
# ◉ ctx
# ◯ axe-syntax
#
# What type of change? (minor)
# Summary: Added new CTX tag support

# Release
udl release
# - Bumps versions
# - Updates CHANGELOGs
# - Creates git tags
# - Publishes to registries
```

## Benefits of This Architecture

1. **Unified Tooling**: One CI/CD setup for all projects
2. **Code Sharing**: Easy to share utilities between projects
3. **Atomic Changes**: Cross-project changes in single PR
4. **Consistent Standards**: Enforced via shared configs
5. **Discoverability**: All projects in one place
6. **History Preservation**: Full git history retained
7. **Independent Evolution**: Projects can still be independent
8. **Language Flexibility**: Each project uses appropriate language
9. **Efficient CI**: Only test what changed
10. **Better Collaboration**: Clear ownership and standards

## Migration Checklist

- [ ] Back up all repositories
- [ ] Commit and push all changes
- [ ] Initialize UDL monorepo
- [ ] Set up workspace package managers
- [ ] Migrate projects preserving history
- [ ] Set up shared tooling
- [ ] Configure CI/CD
- [ ] Update documentation
- [ ] Archive old repositories (don't delete)
- [ ] Update GitHub URLs/redirects
- [ ] Announce to collaborators

## Alternative Approaches

### Hybrid: Monorepo + External Packages

Keep some projects as independent repos:

- Published packages (sandbag, ctx)
- Large applications (black-milk)

Link them as git submodules or workspace packages.

### Meta-Repo

Instead of true monorepo, create a meta-repo with:

- Submodules for each project
- Shared scripts and CI
- Less invasive, easier to back out

## Next Steps

1. **Review this architecture** - Customize to your needs
2. **Choose tooling** - TurboRepo vs Nx vs Custom
3. **Backup everything** - Safety first
4. **Start migration** - One project at a time or all at once
5. **Test thoroughly** - Ensure nothing breaks
6. **Document** - Update all READMEs
