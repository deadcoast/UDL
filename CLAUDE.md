# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

UDL (Universal Development Languages) is a polyglot monorepo containing 30+ independent projects focused on domain-specific languages (DSLs), syntax highlighters, developer tools, and experimental language systems. Each subdirectory is a self-contained project with its own build system, dependencies, and architecture.

## Repository Structure

The repo contains three primary categories of projects:

**DSLs and Language Tools:**

- `axe-Syntax/` - Python CLI menu builder using axe:Syntax notation with Textual TUI
- `CTX/` - CTX-CARD format generator for codebase documentation (Python, AST-based)
- `gate/` and `gateppattern-1.1/` - LSP-based pattern language implementations (TypeScript)
- `f8Syntax/` - F8 language system with execution and metrics (TypeScript)
- `1az/` - VSCode extension for .1az language support
- `DrRx/` - Schema-based DSL with validation

**Godot/Game Development:**

- `black-milk/` - Bitburner-inspired hacking game (GDScript/C#/JS) with custom DSL/VM architecture
- `StrawberryMause/` - Mouse event recording/playback system with grid-based timeline

**Tools and Extensions:**

- `sandbag/` - Intelligent linter configuration manager (Rust) using Bayesian inference
- `camo-obsidian/` - Obsidian plugin for camouflaged codeblocks (TypeScript)
- `ASCII-String-UI-Editor/` - Terminal UI editor and renderer

## Primary Languages

- **Python**: `axe-Syntax`, `CTX`, `JETSON`, `BARRELMAN`, `ctx-card`, `hunt_ascii`, `ASCII-hunt`, `milkDocs`
- **TypeScript**: `gate`, `gateppattern-1.1`, `f8Syntax`, `camo-obsidian`, `StrawberryMause`, `DrRx`, `1az`
- **Rust**: `sandbag`
- **GDScript**: `black-milk`

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

```
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

### Rust Projects (sandbag)

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

## Working with Specific Projects

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

## Build/Development Notes

- Most Python projects use virtual environments - always activate before working
- TypeScript projects may use `pnpm`, `npm`, or `yarn` - check `package-lock.json` or `pnpm-lock.yaml`
- VSCode/Cursor extensions (1az, gate, f8Syntax) require packaging with `vsce` or similar
- Godot projects require Godot engine installed (black-milk)
- Some projects are experimental/WIP - check recent commits for active development

## Navigation Tips

Projects are organized alphabetically but fall into conceptual clusters:

- Language tools: axe, gate, f8Syntax, DrRx, 1az, remedy
- Documentation: CTX, ctx-card, milkDocs
- Games: black-milk
- Tools: sandbag, BARRELMAN, JETSON
- UI/UX: StrawberryMause, ASCII-String-UI-Editor, hunt_ascii
- Obsidian: camo-obsidian

Legacy/deprecated work is in `.depreciated/` directory.
