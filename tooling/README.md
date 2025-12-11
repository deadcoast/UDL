# Tooling

**Purpose:** Development tools, scripts, and utilities for the UDL monorepo
**Status:** Infrastructure
**Category:** Monorepo Infrastructure

## Overview

The `tooling/` directory contains development tools, build scripts, project templates, and utilities that support the UDL monorepo development workflow.

## Directory Structure

```
tooling/
├── scripts/           # Build and utility scripts
├── dev-tools/         # Development tools and CLIs
└── templates/         # Project templates
```

## Scripts (tooling/scripts/)

Shell scripts for common monorepo operations.

### Available Scripts

#### bootstrap.sh
**Purpose:** One-command setup for new developers

```bash
./tooling/scripts/bootstrap.sh
```

**What it does:**
- Installs PNPM if needed
- Installs all Node.js dependencies
- Sets up Python virtual environments
- Installs Rust toolchain
- Configures git hooks
- Validates setup

**See:** [scripts/README.md](./scripts/README.md)

#### migrate-projects.sh
**Purpose:** Migrate projects to monorepo structure

```bash
./tooling/scripts/migrate-projects.sh
```

**What it does:**
- Moves projects to categorized directories
- Preserves git history
- Updates configurations
- Validates migration

### Creating New Scripts

```bash
cd tooling/scripts

# Create new script
cat > my-script.sh <<'EOF'
#!/bin/bash
set -euo pipefail

# Script description
# Usage: ./my-script.sh [args]

# Script logic here
EOF

# Make executable
chmod +x my-script.sh
```

### Script Guidelines

- Use `#!/bin/bash` shebang
- Enable strict mode: `set -euo pipefail`
- Add usage documentation
- Handle errors gracefully
- Test on macOS and Linux
- Follow shell script best practices

## Dev Tools (tooling/dev-tools/)

Custom development tools and CLIs for managing the monorepo.

### Planned Tools

#### monorepo-cli
Command-line interface for monorepo management.

```bash
# Planned features
udl create --name my-project --type tool --lang typescript
udl build --filter=changed
udl test --affected
udl docs generate
udl release --project=sandbag
```

#### generators
Code generators for creating boilerplate.

```bash
# Planned features
udl generate component --name MyComponent
udl generate test --for src/myfile.ts
udl generate docs --format markdown
```

### Building Dev Tools

```bash
cd tooling/dev-tools/monorepo-cli

# TypeScript CLI
pnpm install
pnpm build
pnpm link --global

# Or Python CLI
pip install -e .
```

## Templates (tooling/templates/)

Project templates for creating new UDL projects.

### Available Templates

#### udl-directory-template
Standard template for all UDL projects.

Located at: `projects/experimental/udl-directory-template/`

**See:** [templates/README.md](./templates/README.md) *(to be created)*

### Planned Templates

```
templates/
├── python-project/
├── typescript-project/
├── rust-project/
├── godot-project/
├── vscode-extension/
└── obsidian-plugin/
```

### Using Templates

```bash
# Manual copy
cp -r tooling/templates/python-project projects/tools/my-tool

# Or with CLI (planned)
udl create --template python-project --name my-tool
```

## Common Operations

### Setup New Development Environment

```bash
# Clone repository
git clone https://github.com/deadcoast/UDL.git
cd UDL

# Run bootstrap
./tooling/scripts/bootstrap.sh

# Start developing
cd projects/tools/my-project
```

### Add a New Project

```bash
# Use template
cp -r projects/experimental/udl-directory-template projects/CATEGORY/my-project
cd projects/CATEGORY/my-project

# Customize
# - Update README.md
# - Modify package.json/pyproject.toml
# - Remove unused files
```

### Run Checks Across Projects

```bash
# Lint all projects
pnpm run lint

# Test all projects
pnpm run test

# Build all projects
pnpm run build

# Format all code
pnpm run format
```

## Development

### Adding New Tooling

1. **Choose location:**
   - Scripts → `scripts/`
   - CLIs/Tools → `dev-tools/`
   - Templates → `templates/`

2. **Implement:**
   - Write code
   - Add tests
   - Document usage

3. **Integrate:**
   - Add to root package.json scripts if needed
   - Update this README
   - Add to bootstrap.sh if setup-related

### Testing Tooling

```bash
# Test scripts
cd tooling/scripts
bash -n my-script.sh  # Syntax check
./my-script.sh --dry-run  # Dry run

# Test dev tools
cd tooling/dev-tools/monorepo-cli
pnpm test
```

## Guidelines

### Script Best Practices

- **Idempotent** - Safe to run multiple times
- **Verbose** - Print what's happening
- **Error Handling** - Fail fast with clear messages
- **Documentation** - Usage instructions at top
- **Testing** - Test on clean environment

### Tool Best Practices

- **Single Purpose** - Each tool does one thing well
- **Composable** - Tools work together
- **Consistent** - Follow naming conventions
- **Documented** - README + --help flag
- **Tested** - Automated tests

### Template Best Practices

- **Minimal** - Only essential files
- **Documented** - Clear customization steps
- **Complete** - Runnable out of the box
- **Updated** - Keep in sync with monorepo changes

## Integration with CI/CD

Tooling scripts are used in GitHub Actions:

```yaml
# .github/workflows/ci-main.yml
- name: Bootstrap
  run: ./tooling/scripts/bootstrap.sh

- name: Build
  run: pnpm run build
```

## Future Plans

### Scripts
- [ ] Dependency update script
- [ ] Version bump automation
- [ ] Changelog generation
- [ ] Release preparation script
- [ ] Cleanup/maintenance scripts

### Dev Tools
- [ ] Complete monorepo CLI
- [ ] Code generators
- [ ] Project scaffolding
- [ ] Dependency graph visualizer
- [ ] Performance profiler

### Templates
- [ ] Language-specific templates
- [ ] Framework-specific templates
- [ ] Extension templates
- [ ] Game project templates

## Contributing

When adding tooling:

1. Document purpose and usage
2. Add to appropriate subdirectory
3. Update this README
4. Add tests if applicable
5. Consider CI/CD integration
6. Keep it simple and focused

## Related Documentation

- [scripts/README.md](./scripts/README.md)
- [Bootstrap Documentation](./scripts/bootstrap.sh)
- [Migration Documentation](./scripts/migrate-projects.sh)
- [MONOREPO_ARCHITECTURE.md](../docs/MONOREPO_ARCHITECTURE.md)

---

**Status:** Infrastructure - Active Use
**Scripts:** 2 active (bootstrap, migrate)
**Dev Tools:** 0 (planned)
**Templates:** 1 (udl-directory-template)
**Maintained By:** UDL Team
