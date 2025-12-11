# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

UDL (Universal Development Languages) is a polyglot monorepo containing 33 independent projects focused on domain-specific languages (DSLs), syntax highlighters, developer tools, and experimental language systems. Each subdirectory is a self-contained project with its own build system, dependencies, and architecture.

**Current Status:** Production Ready - All build systems operational, CI/CD configured, 33 projects migrated with full history preserved.

**Package Naming:** TypeScript packages use `@udl/` scope (e.g., `@udl/gate-pattern`, `@udl/gate-pattern-1.1`)

## Repository Structure

The repo contains three primary categories of projects:

**DSLs and Language Tools (8 projects):**

- `axe-Syntax/` - Python CLI menu builder using axe:Syntax notation with Textual TUI
- `CTX/` - CTX-CARD format generator for codebase documentation (Python, AST-based)
- `gate/` (v1.0, @udl/gate-pattern) - LSP-based pattern language implementation (TypeScript)
- `gateppattern-1.1/` (v1.1, @udl/gate-pattern-1.1) - Enhanced pattern language (TypeScript)
- `f8Syntax/` - F8 language system with execution and metrics (TypeScript)
- `1az/` - VSCode extension for .1az language support
- `DrRx/` - Schema-based DSL with validation
- `hoc/`, `remedysyntax/` - Additional language tooling

**Godot/Game Development:**

- `black-milk/` - Bitburner-inspired hacking game (GDScript/C#/JS) with custom DSL/VM architecture
- `StrawberryMause/` - Mouse event recording/playback system with grid-based timeline

**Tools and Extensions (10 projects):**

- `sandbag/` - Intelligent linter configuration manager (Rust) using Bayesian inference
- `camo-obsidian/` - Obsidian plugin for camouflaged codeblocks (TypeScript)
- `ASCII-String-UI-Editor/` - Terminal UI editor and renderer
- `FINK/`, `robo_md/`, `BARRELMAN/`, `JETSON/`, `hunt_ascii/`, `ASCII-hunt/`, `ctx-card/` - Various developer utilities and tools

## Primary Languages

- **Python**: `axe-Syntax`, `CTX`, `JETSON`, `BARRELMAN`, `ctx-card`, `hunt_ascii`, `ASCII-hunt`, `milkDocs`
- **TypeScript**: `gate`, `gateppattern-1.1`, `f8Syntax`, `camo-obsidian`, `StrawberryMause`, `DrRx`, `1az`
- **Rust**: `sandbag`
- **GDScript**: `black-milk`

## Monorepo Commands

### Root-Level Commands (TurboRepo + PNPM)

```bash
# Initial setup for new developers
./tooling/scripts/bootstrap.sh

# Install all dependencies across monorepo
pnpm install

# Build all projects (with intelligent caching)
pnpm build

# Build specific project
turbo run build --filter=sandbag
turbo run build --filter=@udl/gate-pattern

# Build only changed projects
turbo run build --filter=[HEAD^1]

# Run tests across all projects
pnpm test

# Test specific project
turbo run test --filter=ctx

# Lint and format all projects
pnpm lint
pnpm format

# Type check TypeScript projects
pnpm typecheck

# Clean all build artifacts
pnpm clean

# Run checks (lint + typecheck)
pnpm check
```

### Working with Specific Projects

```bash
# Navigate to any project
cd projects/tools/sandbag

# Run project-specific commands directly
cargo test
pnpm build

# Or use turbo from root (recommended)
turbo run test --filter=sandbag
```

## Common Development Commands

### Python Projects (CTX, axe-Syntax, etc.)

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
# or for projects with pyproject.toml:
pip install -e ".[dev]"

# Run tests
pytest
pytest --cov=src  # with coverage

# Lint and format
black src/ tests/
isort src/ tests/
flake8 src/ tests/
mypy src/

# Run CLI tools
python -m ctxcard_gen  # CTX project
# or check each project's README for specific commands
```

### TypeScript/Node Projects (gate, camo-obsidian, StrawberryMause)

```bash
# Install dependencies
npm install
# or
pnpm install

# Build
npm run build
npm run dev  # watch mode

# Test
npm test
npm run test:watch

# Lint
npm run lint
npm run lint:fix

# Format
npm run format
```

### Rust Projects (sandbag)

```bash
# Build
cargo build
cargo build --release

# Test
cargo test
cargo test --release

# Run
cargo run -- [args]

# Lint
cargo clippy

# Format
cargo fmt

# Benchmarks
cargo bench
```

## Project-Specific Architecture Notes

### CTX (CTX-CARD Generator)

CTX generates prefix-free, token-efficient documentation format for codebases.

**Core Architecture:**

- `core/scanner.py` - File discovery with `.ctxignore` support
- `core/ast_analyzer.py` - Python AST parsing and symbol extraction
- `core/call_resolver.py` - Cross-module function call analysis (two-pass)
- `core/card_renderer.py` - CTX-CARD format generation

**Key Concepts:**

- CTX-CARD tags: `ID`, `AL`, `NM`, `MO`, `SY`, `SG`, `ED`, `IN`, `CN`, `ER`, `IO`, `DT`, `TK`, `PX`, `EX`, `RV`, `Δ`
- Module/symbol indexing: `#mid`, `#mid.#sid`
- Edge relationships for imports and calls
- Property/descriptor detection, DTO detection (@dataclass, pydantic)

**Testing:**

```bash
pytest -m unit        # Unit tests only
pytest -m integration # Integration tests
pytest -m "not slow"  # Skip slow tests
```

### black-milk (Godot Game)

Bitburner-inspired hacking game with custom DSL and VM.

**Core Architecture (Godot SRP patterns):**

- `src/core/` - Engine-facing singletons (App, Bus, DI, FS, Log, Time, Persist, Rand)
- `src/domain/` - Pure game logic, no Godot API (Model, Rules, Effects)
- `src/dsl/` - Player-facing scripting language (Grammar, Parser, IR, VM, StdLib, Sandbox)
- `src/systems/` - Game systems (Economy, Network, Skills, Missions, Research)
- `src/adapters/` - Domain↔Godot bridges (Commands, Repo, Telemetry)
- `src/ui/` - ASCII/retro UI (Theme, ViewRouter, Terminal, Editor, Panels)

**Execution Flow:**

```text
UI.Terminal → DSL.Grammar/Parser → AST → DSL.IR → DSL.VM
  → Adapters.Commands → Systems → Domain.Effects → Bus.emit → UI redraw
```

**Key Principles:**

- Domain is pure, deterministic, no Godot API
- DSL has no side effects until adapters layer
- Systems are SRP modules with stateless functions
- UI consumes read-only projections, issues commands via Bus
- DI wiring in `App.gd`

### sandbag (Rust Linter Tool)

Intelligent linter configuration management using Bayesian inference.

**Core Architecture:**

- Probabilistic pattern matching for rule extraction
- Mathematical confidence scoring (Bayesian inference)
- AST-based config file parsing (preserves structure/comments)
- Automatic backup management
- Multi-linter extensibility

**Commands:**

```bash
sandbag add MD033              # Add rule by ID
sandbag scan                   # Scan for suggested suppressions
sandbag batch rules.txt        # Process multiple rules
sandbag config restore latest  # Restore from backup
```

### StrawberryMause (TypeScript/Electron)

Mouse event recording and playback with mathematical grid system.

**Architecture:**

- Event capture at OS level (macOS: CGEventTap)
- Grid-based coordinate system with transformations
- Timeline with 60Hz update frequency
- MausDataMap as source of truth
- BerryWindow for transparent overlay UI
- BerryTimeline for event visualization

**Key Concepts:**

- Coordinate spaces: pixel → normalized → grid → timeline
- Event data structure includes position, action, context
- Atomic timeline operations (add, remove, modify, batch)
- Performance: cache calculations, batch operations, lookup tables

**Data Format (JSON):**

```json
{
  "event": {
    "id": "uuid_v4",
    "time": "ms_from_start",
    "position": { "pixel": {}, "normalized": {}, "grid": {} },
    "action": { "type": "click|drag|release", "button": "left|right|middle" },
    "context": { "window": "id", "application": "name" }
  }
}
```

### axe-Syntax (Python)

CLI menu builder using axe:Syntax custom notation.

**Components:**

- `parser/parser.py` - axe:Syntax parser
- `parser/transformer.py` - AST transformation
- `models/models.py` - Data models for menus/commands
- `exporter/exporter.py` - Export to Python CLI templates (Typer)
- `tui/tui.py` - Textual TUI for visualization
- `logger/logger.py` - Loguru-based logging

**Usage:**

```bash
# Build CLI from axe:Syntax
axe build input.axe

# Launch TUI
axe tui

# Parse command
axe parse-command "command syntax"
```

## Code Style and Conventions

### Python Projects

Follow PEP 8 and project-specific `.cursorrules` (JSON format in CTX).

**Key conventions:**

- 4 spaces indentation
- 88-character line length (Black default) or 120 (some projects)
- Type hints required
- Docstrings for all public APIs (Google or NumPy style)
- Avoid bare `except`, use specific exceptions
- Prefer composition over inheritance

### TypeScript Projects

**Key conventions:**

- 2 or 4 spaces (check project's `.prettierrc` or `package.json`)
- ESLint + Prettier for consistency
- Strict TypeScript mode
- Interfaces for data structures, types for unions
- JSDoc comments for public APIs

### Rust Projects Code Style (sandbag)

**Key conventions:**

- Standard Rust formatting (`cargo fmt`)
- Clippy for linting
- Result/Option for error handling
- Type-driven design
- Zero-cost abstractions where possible

## Testing Practices

### Python

- Use `pytest` with markers: `@pytest.mark.unit`, `@pytest.mark.integration`, `@pytest.mark.slow`
- Aim for 80-90% coverage minimum
- Mock external dependencies
- Test pure functions separately from I/O

### TypeScript

- Use Jest or Vitest depending on project
- Test UI components with snapshot tests where appropriate
- Integration tests for LSP servers (gate, f8Syntax)

### Rust

- Unit tests in same file (`#[cfg(test)] mod tests`)
- Integration tests in `tests/` directory
- Benchmarks in `benches/` directory
- Use `cargo test --release` for accurate performance tests

## Project-Specific Development

When working on a project:

1. **Check for project-specific docs**: Most projects have their own `README.md`, `docs/` directory, or architecture documentation
2. **Review `.cursorrules`**: Several projects (CTX, black-milk, sandbag, StrawberryMause) have comprehensive cursor rules with JSON-based style guides
3. **Check `DESIGN-ARCHITECTURE.md`**: Projects like black-milk have detailed architecture docs explaining the "big picture"
4. **Review AI collaboration guides**: StrawberryMause has `Docs/AI-Collaberation-Guide.md` with special JSON bracket notation system

## Important Cross-Project Patterns

### Modular Architecture

All major projects follow SRP (Single Responsibility Principle):

- Core/domain logic separate from UI/adapters
- Pure functions for testability
- Event-driven communication (Bus/signals)
- Dependency injection where applicable

### Custom DSL Pattern

Multiple projects implement custom DSLs:

- Define grammar (EBNF or similar)
- Parse to AST
- Transform to IR (intermediate representation)
- Execute via VM or interpreter
- Separate parsing from execution

### Documentation Generation

CTX-CARD format appears in multiple projects:

- Token-efficient, prefix-free aliases
- Module and symbol indexing
- Edge relationships (imports, calls)
- Naming grammar with regex patterns
- Designed for AI consumption

## Monorepo-Specific Patterns

### TurboRepo Task Pipeline

The monorepo uses TurboRepo for intelligent build orchestration:

- **Dependency ordering**: `build` tasks run dependencies first (`dependsOn: ["^build"]`)
- **Caching**: Build outputs are cached; unchanged projects skip rebuilds
- **Parallel execution**: Independent tasks run concurrently
- **Incremental builds**: Only changed projects rebuild

```bash
# Build with full dependency graph
turbo run build

# Test (depends on build completing first)
turbo run test

# Check (runs lint + typecheck in parallel)
turbo run check
```

### PNPM Workspace Management

Projects reference each other using workspace protocol:

```json
{
  "dependencies": {
    "@udl/shared-utils": "workspace:*"
  }
}
```

When adding internal dependencies, use `workspace:*` for automatic version resolution.

### Git Submodule Handling

Many projects contain embedded `.git` directories from the migration. This is expected:

- Warnings like `adding embedded git repository: projects/tools/sandbag` are normal
- CI/CD uses `submodules: false` to prevent initialization issues
- Don't delete these `.git` directories; they preserve full project history

## Build/Development Notes

- **Bootstrap first**: Run `./tooling/scripts/bootstrap.sh` for initial setup
- **Use turbo from root**: Prefer `turbo run build --filter=project` over per-project commands
- **Check pipeline dependencies**: Some tasks depend on others (test needs build)
- Most Python projects use virtual environments - always activate before working
- TypeScript projects use PNPM (required version: 8.15.1)
- VSCode/Cursor extensions (1az, gate, f8Syntax) require packaging with `vsce` or similar
- Godot projects require Godot engine installed (black-milk)
- Some projects are experimental/WIP - check recent commits for active development

## Navigation Tips

Projects are organized by category in `projects/`:

**By Category:**
- `projects/languages/` - DSL implementations (8 projects)
- `projects/tools/` - CLI utilities and generators (9 projects)
- `projects/extensions/` - Editor plugins (1 project)
- `projects/applications/` - Full applications (3 projects)
- `projects/libraries/` - Reusable libraries (3 projects)
- `projects/experimental/` - WIP/Research (9 projects)

**By Conceptual Cluster:**
- Language tools: axe, gate, f8Syntax, DrRx, 1az, remedy
- Documentation: CTX, ctx-card, milkDocs
- Games: black-milk
- Tools: sandbag, BARRELMAN, JETSON
- UI/UX: StrawberryMause, ASCII-String-UI-Editor, hunt_ascii
- Obsidian: camo-obsidian

**Project Structure Pattern:**
Each project typically contains:
- `README.md` - Project-specific documentation
- `.cursorrules` or `.cursor/rules/` - AI coding guidelines (if present)
- Project-specific build configuration (package.json, Cargo.toml, pyproject.toml)

Legacy/deprecated work is in `.depreciated/` directory.

## Documentation Structure

**Root Level (Essential):**

- `CLAUDE.md` - This file, AI assistant instructions
- `README.md` - Main repository documentation

**docs/ Directory (Detailed Documentation):**

- `MONOREPO-STATUS.md` - Current status, recent updates, and known issues
- `MONOREPO_ARCHITECTURE.md` - Architecture design and technical decisions
- `MIGRATION_SUCCESS.md` - Migration completion summary
- `MIGRATION_PLAN.md` - Original migration strategy

## Recent Infrastructure Updates

**Package Naming (December 2025):**

- Resolved package name conflicts by implementing `@udl/` scoped packages
- `gate` → `@udl/gate-pattern` (v1.0.0)
- `gateppattern-1.1` → `@udl/gate-pattern-1.1` (v1.1.0)
- Future TypeScript packages should use `@udl/` scope

**CI/CD Fixes (December 2025):**

- Fixed PNPM version mismatch: all workflows now use exact version `8.15.1`
- Fixed git submodule errors: added `submodules: false` to all checkout actions
- All GitHub Actions workflows now operational

**Build System (December 2025):**

- TurboRepo + PNPM workspace fully operational
- Build verification: 2/3 TypeScript projects building successfully
- Added tsconfig.json for camo-obsidian (projects/extensions/camo-obsidian/tsconfig.json)
- Build command: `pnpm run build --filter="./projects/**"`

## Monorepo Configuration Files

**Root Level:**
- `package.json` - Root workspace, defines scripts and workspaces
- `pnpm-workspace.yaml` - PNPM workspace configuration (all projects/*)
- `turbo.json` - TurboRepo pipeline configuration and caching rules
- `Cargo.toml` - Rust workspace (currently only sandbag)
- `pyproject.toml` - Python workspace configuration

**Key Scripts in package.json:**
- `pnpm build` → `turbo run build` (with caching)
- `pnpm test` → `turbo run test` (depends on build)
- `pnpm bootstrap` → `./tooling/scripts/bootstrap.sh`
- `pnpm check` → runs lint + typecheck

## CI/CD Integration

The monorepo uses smart change detection:

**.github/workflows/ci-main.yml** - Orchestrator that:
1. Detects which file types changed (Python, TypeScript, Rust, Godot)
2. Calls language-specific workflows only for changed code
3. Runs conventional commit checks and formatting

**Language-Specific Workflows:**
- `ci-python.yml` - Runs pytest on Python 3.8-3.12
- `ci-typescript.yml` - Runs builds/tests on Node 18-20
- `ci-rust.yml` - Runs cargo test + clippy on stable/beta

This means CI only tests what actually changed, significantly reducing build times.
