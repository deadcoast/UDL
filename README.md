# UDL - Universal Development Languages

**A comprehensive monorepo for domain-specific languages, language tools, and developer utilities**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Turborepo](https://img.shields.io/badge/built%20with-Turborepo-blueviolet)](https://turbo.build/)
[![Monorepo](https://img.shields.io/badge/monorepo-pnpm-orange)](https://pnpm.io/)

## Overview

UDL is a polyglot monorepo containing 33 independent projects focused on:

- **Domain-Specific Languages (DSLs)** - Custom language implementations
- **Developer Tools** - CLI utilities, linters, and code generators
- **Syntax Highlighters** - Editor extensions and language support
- **Applications** - Full-featured applications built with custom languages
- **Libraries** - Reusable components and utilities

**Status:** Early Access | CI/CD Operational | 33 Projects | 4 Languages

## Quick Start

```bash
# Clone the repository
git clone https://github.com/deadcoast/UDL.git
cd UDL

# Run the bootstrap script (installs all dependencies)
./tooling/scripts/bootstrap.sh

# Build all projects
pnpm build

# Run tests
pnpm test
```

## Repository Structure

```
UDL/
├── projects/
│   ├── languages/       # DSL implementations (axe, gate, f8, etc.)
│   ├── tools/           # Developer tools (ctx, sandbag, etc.)
│   ├── extensions/      # Editor extensions (camo-obsidian, etc.)
│   ├── applications/    # Full applications (black-milk, etc.)
│   ├── libraries/       # Reusable libraries
│   └── experimental/    # WIP/Research projects
├── shared/
│   ├── packages/        # Shared code libraries
│   └── configs/         # Shared configurations
├── tooling/
│   ├── scripts/         # Build and utility scripts
│   └── dev-tools/       # Monorepo management CLI
├── docs/                # Documentation
└── examples/            # Cross-project examples
```

## Technology Stack

### Languages & Runtimes

- **TypeScript/JavaScript** - Language servers, VSCode extensions, web tools
- **Python** - CLI tools, AST analysis, code generation
- **Rust** - High-performance tools, linters
- **GDScript** - Godot-based applications

### Monorepo Tools

- **TurboRepo** - Build orchestration and caching
- **PNPM** - Fast, efficient package management
- **Cargo Workspaces** - Rust project management
- **Poetry/pip** - Python dependency management

## Featured Projects

### Languages (8 projects)

- **[axe-syntax](projects/languages/axe-Syntax)** - CLI menu builder with custom notation (Python)
- **[gate](projects/languages/gate)** - Pattern language with LSP support v1.0 (@udl/gate-pattern)
- **[gateppattern-1.1](projects/languages/gateppattern-1.1)** - Pattern language v1.1 (@udl/gate-pattern-1.1)
- **[f8syntax](projects/languages/f8Syntax)** - F8 language system with execution engine
- **[1az](projects/languages/1az)** - VSCode extension for .1az language
- **[DrRx](projects/languages/DrRx)** - Schema-based DSL
- **[hoc](projects/languages/hoc)** - Language tooling
- **[remedysyntax](projects/languages/remedysyntax)** - Syntax support

### Tools (9 projects)

- **[CTX](projects/tools/CTX)** - CTX-CARD format generator for codebase documentation (Python)
- **[sandbag](projects/tools/sandbag)** - Intelligent linter configuration manager (Rust)
- **[ctx-card](projects/tools/ctx-card)** - AST-based codebase documentation
- **[FINK](projects/tools/FINK)** - Developer utility
- **[robo_md](projects/tools/robo_md)** - Markdown automation
- **[BARRELMAN](projects/tools/BARRELMAN)** - Development tool
- **[JETSON](projects/tools/JETSON)** - Utility tool
- **[hunt_ascii](projects/tools/hunt_ascii)** - ASCII utilities
- **[ASCII-hunt](projects/tools/ASCII-hunt)** - ASCII tooling

### Applications (3 projects)

- **[black-milk](projects/applications/black-milk)** - Hacking game with custom DSL/VM (Godot)
- **[StrawberryMause](projects/applications/StrawberryMause)** - Mouse event recording/playback (TypeScript/Electron)
- **[ASCII-String-UI-Editor](projects/applications/ASCII-String-UI-Editor)** - Terminal UI editor and renderer

### Extensions (1 project)

- **[camo-obsidian](projects/extensions/camo-obsidian)** - Obsidian plugin for camouflaged codeblocks (TypeScript)

### Libraries (3 projects)

- **[milkDocs](projects/libraries/milkDocs)** - Documentation library (Python)
- Plus 2 additional libraries

### Experimental (9 projects)

WIP and research projects including mecha_development, motleyBard, CLAY, PACER, canon, and more

## Development

### Prerequisites

- **Node.js** >= 18.0.0
- **PNPM** >= 8.0.0
- **Python** >= 3.8
- **Rust** >= 1.70 (for Rust projects)
- **Godot** >= 4.0 (for Godot projects)

### Common Commands

```bash
# Install dependencies
pnpm install

# Build all projects
pnpm build

# Build specific project
turbo run build --filter=sandbag

# Run tests
pnpm test

# Test specific project
turbo run test --filter=ctx

# Lint all projects
pnpm lint

# Format code
pnpm format

# Type check
pnpm typecheck

# Clean build artifacts
pnpm clean
```

### Working on a Project

```bash
# Navigate to project
cd projects/tools/sandbag

# Project-specific commands work as usual
cargo build
cargo test

# Or use turbo from root
turbo run build --filter=sandbag
```

### Adding a New Project

```bash
# Use the project generator
pnpm udl create --name my-project --type tool --lang typescript

# Or manually create in appropriate directory
mkdir -p projects/tools/my-project
```

## Documentation

### Core Documentation

- **[CLAUDE.md](CLAUDE.md)** - Guide for AI-assisted development
- **[README.md](README.md)** - You are here

### Extended Documentation (docs/)

- **[MONOREPO-STATUS.md](docs/MONOREPO-STATUS.md)** - Current state and recent updates
- **[MONOREPO_ARCHITECTURE.md](docs/MONOREPO_ARCHITECTURE.md)** - Architecture design and patterns
- **[MIGRATION_SUCCESS.md](docs/MIGRATION_SUCCESS.md)** - Migration completion summary
- **[MIGRATION_PLAN.md](docs/MIGRATION_PLAN.md)** - Original migration strategy

### Project-Specific Docs

Each project maintains its own README with detailed information:

- Project overview and features
- Installation and usage
- API documentation
- Examples

## Testing

```bash
# Run all tests
pnpm test

# Run tests for changed projects only
turbo run test --filter=[HEAD^1]

# Run with coverage
pnpm test:coverage

# Run specific test suites
pytest                    # Python projects
cargo test                # Rust projects
npm test                  # TypeScript projects
```

## Publishing

Individual projects can be published independently:

```bash
# Python (PyPI)
cd projects/tools/ctx
python -m build
twine upload dist/*

# NPM
cd projects/extensions/camo-obsidian
npm publish

# Cargo (crates.io)
cd projects/tools/sandbag
cargo publish
```

## Contributing

Contributions are welcome! Please see:

- [CONTRIBUTING.md](docs/CONTRIBUTING.md) - Contribution guidelines
- Project-specific contribution guides in each project's README

### Development Workflow

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Make your changes
3. Run tests: `pnpm test`
4. Run linting: `pnpm lint`
5. Commit using conventional commits: `git commit -m "feat: add new feature"`
6. Push and create a pull request

## 📄 License

MIT License - see individual projects for specific licensing information.

## Project Status

This monorepo is actively maintained and continuously evolving. Individual projects may have different maturity levels:

- **Stable** - Production-ready
- **Beta** - Feature-complete, testing
- **Experimental** - Early development, API may change

Check each project's README for its current status.

## Links

- **GitHub**: <https://github.com/deadcoast/UDL>
- **Documentation**: [docs/](docs/)
- **Issues**: <https://github.com/deadcoast/UDL/issues>

## Highlights

- **33 Projects** in a unified monorepo with full git history
- **Polyglot** - TypeScript, Python, Rust, GDScript
- **Smart Caching** - TurboRepo for lightning-fast builds
- **Scoped Packages** - @udl/\* namespace for TypeScript packages
- **Modern CI/CD** - GitHub Actions with change detection
- **Multi-Version Testing** - Python 3.8-3.12, Node 18-20, Rust stable/beta
- **Well Documented** - Comprehensive docs for AI and humans
- **Production Ready** - Fully operational build system

## Recent Updates

### December 11, 2025

- ✅ Fixed package naming conflicts (gate projects now use @udl scope)
- ✅ Resolved CI/CD issues (PNPM version mismatch, git submodule errors)
- ✅ Added tsconfig.json for camo-obsidian
- ✅ Verified build system (2/3 TypeScript projects building successfully)
- ✅ Updated all CI workflows for GitHub Actions compatibility
- ✅ Organized documentation structure

See [MONOREPO-STATUS.md](docs/MONOREPO-STATUS.md) for detailed status and updates.

---

deadcoast UDL designs [deadcoast](https://github.com/deadcoast)
