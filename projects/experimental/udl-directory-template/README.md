# UDL Directory Template

**Type:** Project Template
**Status:** 📦 Template
**Category:** Experimental / Infrastructure

## Overview

This is the standard template for creating new UDL projects. It provides a consistent structure, configuration files, and boilerplate code that all UDL projects should follow.

## Usage

### Creating a New Project

```bash
# From UDL root
cp -r projects/experimental/udl-directory-template projects/CATEGORY/my-new-project
cd projects/CATEGORY/my-new-project

# Customize the template
# 1. Update README.md with project details
# 2. Modify package.json/pyproject.toml/Cargo.toml as needed
# 3. Remove unused files for your language
# 4. Initialize git if needed
```

### What's Included

```
udl-directory-template/
├── README.md                 # This file - template README
├── .gitignore               # Comprehensive gitignore
├── .gitattributes           # Line ending management
├── .editorconfig            # Editor configuration
├── .markdownlint.json       # Markdown linting rules
│
# Choose your language stack:
├── package.json             # TypeScript/JavaScript projects
├── tsconfig.json            # TypeScript configuration
├── pyproject.toml           # Python projects
├── Cargo.toml               # Rust projects
│
# Optional configurations:
├── .vscode/                 # VSCode settings
│   └── settings.json
├── .github/                 # GitHub workflows (if standalone)
│   └── workflows/
│       └── ci.yml
│
# Standard directories:
├── src/                     # Source code
├── tests/                   # Test files
├── docs/                    # Documentation
├── examples/                # Usage examples
└── LICENSE                  # License file
```

## Template Components

### README Template

Every project should have a README with:

- Project name and description
- Status badge (🔬 Experimental, 🚧 Beta, ✅ Stable)
- Installation instructions
- Quick start guide
- API documentation or usage
- Contributing guidelines
- License information

### Configuration Files

#### .gitignore

Comprehensive ignore rules for:

- Node.js (node_modules, dist)
- Python (**pycache**, .venv)
- Rust (target, Cargo.lock for libraries)
- IDEs (.vscode, .idea)
- OS files (.DS_Store, Thumbs.db)

#### .editorconfig

Consistent editor settings:

- UTF-8 encoding
- LF line endings
- Trim trailing whitespace
- Insert final newline

#### TypeScript Projects

```json
{
  "name": "@udl/project-name",
  "version": "0.1.0",
  "scripts": {
    "build": "tsc",
    "test": "jest",
    "lint": "eslint src/",
    "format": "prettier --write src/"
  }
}
```

#### Python Projects

```toml
[project]
name = "project-name"
version = "0.1.0"
dependencies = []

[project.optional-dependencies]
dev = ["pytest", "black", "mypy", "isort"]
```

#### Rust Projects

```toml
[package]
name = "project-name"
version = "0.1.0"
edition = "2021"

[dependencies]
```

## Directory Structure Guidelines

### Source Code (src/)

```
src/
├── index.ts / __init__.py / lib.rs   # Entry point
├── core/                              # Core functionality
├── utils/                             # Utility functions
├── types/                             # Type definitions
└── ... (project-specific)
```

### Tests (tests/)

```
tests/
├── unit/                   # Unit tests
├── integration/            # Integration tests
├── fixtures/               # Test data
└── __init__.py / mod.rs    # Test module init
```

### Documentation (docs/)

```
docs/
├── README.md              # Documentation index
├── getting-started.md     # Quick start guide
├── api.md                 # API documentation
├── architecture.md        # Architecture overview
└── examples/              # Detailed examples
```

## Customization Checklist

When using this template:

- [ ] Update README.md with project details
- [ ] Modify package.json/pyproject.toml/Cargo.toml
- [ ] Set appropriate project name (use @udl/ scope for TypeScript)
- [ ] Update LICENSE file
- [ ] Remove unused language configurations
- [ ] Customize .gitignore if needed
- [ ] Add project-specific CI/CD workflows
- [ ] Create initial source files in src/
- [ ] Write initial tests
- [ ] Document in docs/

## Naming Conventions

### Project Names

- **Languages:** lowercase-with-dashes (e.g., `my-language`)
- **Tools:** lowercase or PascalCase (e.g., `my-tool` or `MyTool`)
- **Applications:** PascalCase (e.g., `MyApp`)
- **Libraries:** lowercase_with_underscores (Python) or lowercase-with-dashes (others)

### Package Names

- **TypeScript:** `@udl/package-name`
- **Python:** `package_name` (underscores)
- **Rust:** `package-name` (dashes)

## Best Practices

### Version Control

- Start at version 0.1.0
- Use semantic versioning
- Tag releases
- Write changelog

### Testing

- Write tests from the start
- Aim for >70% coverage
- Include integration tests
- Add CI/CD early

### Documentation

- Document as you code
- Provide examples
- Explain architecture
- Keep README updated

### Code Quality

- Use linters
- Format consistently
- Type hint (Python/TypeScript)
- Handle errors properly

## Related Templates

- **GitHub Project Templates** - For standalone repos
- **VSCode Extension Template** - For editor extensions
- **Godot Project Template** - For game projects

## Updating the Template

When the template needs updates:

1. Make changes in this directory
2. Document in this README
3. Notify in main repo CHANGELOG
4. Consider migrating existing projects

---

**Type:** Template
**Last Updated:** December 2025
**Compatibility:** All UDL project types
**Maintained By:** UDL Team
