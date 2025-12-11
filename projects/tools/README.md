# Tools

Developer tools, CLI utilities, and code generators.

## Projects

### Stable

- **[sandbag](sandbag/)** ⭐ - Intelligent linter configuration manager (Rust)
  - Bayesian inference for rule extraction
  - Multi-linter support
  - Automatic backup management

- **[CTX](CTX/)** ⭐ - CTX-CARD format generator for codebase documentation (Python)
  - AST-based analysis
  - Cross-module call resolution
  - Token-efficient documentation

- **[ctx-card](ctx-card/)** - Enhanced CTX-CARD generation with additional features

### Active Development

- **[axe](axe/)** - Axe language tooling
- **[axe_syntax](axe_syntax/)** - Axe syntax parser and processor
- **[JETSON](JETSON/)** - JSON editing and transformation tool
- **[BARRELMAN](BARRELMAN/)** - Build and release management
- **[robo_md](robo_md/)** - Markdown automation and processing
- **[FINK](FINK/)** - File integrity checker

## Categories

- **Linters & Formatters**: sandbag
- **Documentation**: CTX, ctx-card
- **Build Tools**: BARRELMAN
- **File Processing**: robo_md, FINK

## Development

### Rust Tools (sandbag)

```bash
cd projects/tools/sandbag
cargo build --release
cargo test
```

### Python Tools (CTX, ctx-card)

```bash
cd projects/tools/CTX
pip install -e ".[dev]"
pytest
```

## Publishing

Tools are published to their respective package registries:

- Rust tools → crates.io
- Python tools → PyPI
- Node tools → npm

See individual project READMEs for publishing instructions.
