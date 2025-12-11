# Shared Resources

**Purpose:** Shared code, configurations, and assets used across multiple UDL projects
**Status:** Infrastructure
**Category:** Monorepo Infrastructure

## Overview

The `shared/` directory contains resources that are used by multiple projects in the UDL monorepo. This includes shared code libraries, common configurations, and reusable assets.

## Directory Structure

```
shared/
├── packages/          # Shared code libraries
├── configs/           # Common configuration files
└── assets/            # Shared assets (fonts, icons, etc.)
```

## Packages (shared/packages/)

Shared code libraries that can be used as dependencies by UDL projects.

### Creating a Shared Package

```bash
cd shared/packages
mkdir my-shared-lib
cd my-shared-lib

# For TypeScript
cat > package.json <<EOF
{
  "name": "@udl/my-shared-lib",
  "version": "0.1.0",
  "main": "dist/index.js",
  "types": "dist/index.d.ts"
}
EOF

# For Python
cat > pyproject.toml <<EOF
[project]
name = "udl-my-shared-lib"
version = "0.1.0"
EOF
```

### Using Shared Packages

#### In TypeScript Projects
```json
{
  "dependencies": {
    "@udl/my-shared-lib": "workspace:*"
  }
}
```

#### In Python Projects
```toml
[project.dependencies]
udl-my-shared-lib = {path = "../../shared/packages/my-shared-lib", develop = true}
```

## Configurations (shared/configs/)

Common configuration files for linters, formatters, and build tools.

### Planned Configurations

```
configs/
├── .prettierrc.json       # Prettier formatting (TypeScript)
├── .eslintrc.json         # ESLint linting (TypeScript)
├── pyproject.toml         # Base Python config
├── rust-clippy.toml       # Clippy config (Rust)
└── tsconfig.base.json     # Base TypeScript config
```

### Usage

Projects can extend these base configurations:

**TypeScript:**
```json
{
  "extends": "../../shared/configs/tsconfig.base.json"
}
```

**Python:**
```toml
[tool.black]
extend = "../../shared/configs/pyproject.toml"
```

## Assets (shared/assets/)

Shared assets like fonts, icons, and branding materials.

### Planned Assets

```
assets/
├── branding/
│   ├── logos/
│   ├── colors.json
│   └── typography.json
├── fonts/
└── icons/
```

### Usage

```typescript
// In a TypeScript project
import logo from '../../shared/assets/branding/logos/udl-logo.svg';
```

```python
# In a Python project
ASSETS_PATH = Path(__file__).parent.parent / "shared" / "assets"
```

## Guidelines

### When to Share

Create shared resources when:
- Code is used by 2+ projects
- Configuration should be consistent across projects
- Assets are reused in multiple places
- Reducing duplication significantly

### When NOT to Share

Keep resources local when:
- Only one project uses it
- Projects have different requirements
- Coupling would be problematic
- Independence is more valuable

### Naming Conventions

- **TypeScript Packages:** `@udl/package-name`
- **Python Packages:** `udl_package_name`
- **Rust Crates:** `udl-package-name`
- **Assets:** `kebab-case.ext`

## Development

### Building Shared Packages

```bash
# Build all TypeScript shared packages
cd shared/packages
for dir in */; do
  cd "$dir"
  if [ -f "package.json" ]; then
    pnpm build
  fi
  cd ..
done
```

### Testing Shared Packages

```bash
# Test all shared packages
cd shared/packages
for dir in */; do
  cd "$dir"
  pnpm test || pytest || cargo test
  cd ..
done
```

## Future Plans

### Shared Packages (Planned)

- **@udl/ctx-common** - Common CTX utilities (Python)
- **@udl/dsl-toolkit** - DSL parsing utilities (TypeScript)
- **@udl/udl-testing** - Testing utilities (Mixed)
- **@udl/ast-helpers** - AST manipulation helpers (TypeScript)

### Shared Configs (Planned)

- Unified linting rules
- Common formatter configs
- Shared TypeScript settings
- Python tooling configs

### Shared Assets (Planned)

- UDL branding guidelines
- Common icons and graphics
- Shared fonts
- UI design tokens

## Contributing

When adding shared resources:

1. Ensure they're truly shared (used by 2+ projects)
2. Document the purpose and usage
3. Version appropriately (semantic versioning)
4. Add tests if applicable
5. Update this README

## Related Documentation

- [MONOREPO_ARCHITECTURE.md](../docs/MONOREPO_ARCHITECTURE.md)
- [Project Templates](../tooling/templates/)
- [Build Scripts](../tooling/scripts/)

---

**Status:** Infrastructure
**Current Packages:** 0 (planned)
**Current Configs:** 0 (planned)
**Current Assets:** 0 (planned)
**Maintained By:** UDL Team
