# UDL Libraries

Reusable code libraries and shared utilities used across UDL projects. These libraries provide common functionality for ASCII manipulation, documentation generation, and various utility operations.

## Overview

This directory contains standalone libraries that can be used independently or as dependencies for other UDL projects. Libraries are designed to be modular, well-tested, and easy to integrate.

## Projects in this Category

### [milkDocs](./milkDocs)

**Type:** Documentation Library
**Language:** Python
**Status:** 🚧 Beta

Documentation generation and management library for Python projects.

**Features:**
- Automated documentation generation
- Markdown output
- API documentation
- Cross-referencing

**Quick Start:**
```bash
cd milkDocs
pip install -e .
```

**Documentation:** [milkDocs/README.md](./milkDocs/README.md)

---

### [hunt_ascii](./hunt_ascii)

**Type:** ASCII Utility Library
**Language:** Python
**Status:** ✅ Stable

Utilities for ASCII art generation, manipulation, and analysis.

**Features:**
- ASCII art rendering
- Text-to-ASCII conversion
- ASCII manipulation tools
- Pattern matching

**Quick Start:**
```bash
cd hunt_ascii
pip install -e .
```

**Documentation:** [hunt_ascii/README.md](./hunt_ascii/README.md)

---

### [ASCII-hunt](./ASCII-hunt)

**Type:** ASCII Processing Library
**Language:** Python
**Status:** ✅ Stable

Advanced ASCII processing and search functionality.

**Features:**
- ASCII pattern searching
- Text processing
- Character analysis
- Format conversion

**Quick Start:**
```bash
cd ASCII-hunt
pip install -e .
```

**Documentation:** [ASCII-hunt/README.md](./ASCII-hunt/README.md)

## Development

### Building All Libraries

From the repository root:
```bash
# Install all Python libraries
cd projects/libraries
for dir in */; do
  cd "$dir"
  pip install -e .
  cd ..
done

# Run tests for all libraries
for dir in */; do
  cd "$dir"
  pytest
  cd ..
done
```

### Using Libraries as Dependencies

#### Python Projects
```python
# In your project's requirements.txt or pyproject.toml
milkDocs @ file:///path/to/UDL/projects/libraries/milkDocs
hunt_ascii @ file:///path/to/UDL/projects/libraries/hunt_ascii
```

#### From Within Monorepo
```toml
# pyproject.toml
[tool.poetry.dependencies]
milkDocs = { path = "../../libraries/milkDocs", develop = true }
```

### Creating a New Library

```bash
# Navigate to libraries directory
cd projects/libraries

# Create new library
mkdir my-library
cd my-library

# Initialize Python package
cat > setup.py <<EOF
from setuptools import setup, find_packages

setup(
    name="my-library",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
)
EOF

# Create package structure
mkdir my_library
touch my_library/__init__.py
```

## Library Standards

All libraries in this category should follow these standards:

### Structure
```
library-name/
├── src/                    # Source code
│   └── library_name/
│       ├── __init__.py
│       ├── core.py
│       └── utils.py
├── tests/                  # Test suite
│   ├── test_core.py
│   └── test_utils.py
├── docs/                   # Documentation
├── README.md              # Library documentation
├── setup.py or pyproject.toml
├── requirements.txt       # Dependencies
└── LICENSE                # License file
```

### Testing
- Minimum 80% code coverage
- Unit tests for all public APIs
- Integration tests for complex features
- Example usage in documentation

### Documentation
- Clear README with examples
- API documentation (docstrings)
- Usage examples
- Installation instructions
- Changelog

### Versioning
- Semantic versioning (MAJOR.MINOR.PATCH)
- Changelog maintained
- Git tags for releases

## Common Patterns

### ASCII Processing
Libraries dealing with ASCII art, text manipulation, and character-based rendering:
- `hunt_ascii` - ASCII art utilities
- `ASCII-hunt` - ASCII search and processing

### Documentation
Libraries for generating and managing documentation:
- `milkDocs` - Documentation generation

### Utilities
General-purpose utility libraries (future expansion)

## Testing

```bash
# Test a specific library
cd milkDocs
pytest -v --cov=src

# Test with coverage report
pytest --cov=src --cov-report=html

# Run type checking
mypy src/
```

## Publishing

Libraries can be published to PyPI independently:

```bash
cd library-name

# Build distribution
python -m build

# Upload to PyPI
twine upload dist/*
```

## Contributing

When adding a new library:

1. Follow Python packaging best practices
2. Include comprehensive tests (>80% coverage)
3. Write clear documentation with examples
4. Add type hints to all public APIs
5. Update this category README
6. Consider dependencies carefully (keep them minimal)

## Inter-Library Dependencies

Some libraries depend on each other:

```
milkDocs (standalone)
hunt_ascii (standalone)
ASCII-hunt (standalone)
```

When adding dependencies between libraries, document them clearly and avoid circular dependencies.

## Related Projects

- **[tools](../tools)** - CLI tools that use these libraries
- **[languages](../languages)** - DSLs that may use library utilities
- **[applications](../applications)** - Applications built with these libraries

## Links

- [Python Packaging Guide](https://packaging.python.org/)
- [Semantic Versioning](https://semver.org/)
- [PyPI](https://pypi.org/)

---

**Total Libraries:** 3
**Primary Language:** Python
**Package Manager:** pip / Poetry
**Test Framework:** pytest
