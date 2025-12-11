# UDL Experimental Projects

Work-in-progress and research projects exploring new ideas, experimental language features, and proof-of-concept implementations. These projects are in active development and may have incomplete features or changing APIs.

## ⚠️ Important Notice

Projects in this directory are **experimental** and may:
- Have incomplete or changing APIs
- Lack comprehensive documentation
- Contain experimental features
- Undergo significant restructuring
- Be merged, archived, or graduated to other categories

**Use at your own risk in production environments.**

## Overview

The experimental directory serves as an incubator for:
- New language concepts and DSL designs
- Proof-of-concept implementations
- Research projects
- Prototypes for future stable projects
- Explorations of novel programming paradigms

## Projects in this Category

### [mecha_development](./mecha_development)

**Type:** Language Development Framework
**Language:** Mixed (Python/TypeScript)
**Status:** 🔬 Experimental

Framework for developing and testing mechanical language constructs.

**Focus Areas:**
- Language design patterns
- DSL construction utilities
- Parser generation experiments

**Documentation:** [mecha_development/README.md](./mecha_development/README.md)

---

### [mecha_lang](./mecha_lang)

**Type:** DSL Implementation
**Language:** Python/TypeScript
**Status:** 🔬 Experimental

Experimental language implementation exploring mechanical programming concepts.

**Features:**
- Novel syntax constructs
- Experimental parser
- VM prototype

---

### [canon](./canon)

**Type:** Language Tool
**Language:** Mixed
**Status:** 🔬 Experimental

Canonical language representation and transformation toolkit.

**Features:**
- Language canonicalization
- Syntax transformation
- Format standardization

**Documentation:** [canon/README.md](./canon/README.md)

---

### [PACER](./PACER)

**Type:** Development Tool
**Language:** Python
**Status:** 🔬 Experimental

Performance analysis and code evaluation research project.

**Features:**
- Code performance analysis
- Benchmarking utilities
- Profiling tools

**Documentation:** [PACER/README.md](./PACER/README.md)

---

### [CLAY](./CLAY)

**Type:** Language/Framework
**Language:** Mixed
**Status:** 🔬 Experimental

Experimental framework exploring composable language abstractions.

**Focus Areas:**
- Language composition
- Abstraction layers
- Modular language design

---

### [motleyBard](./motleyBard)

**Type:** Code Generation Tool
**Language:** Python
**Status:** 🔬 Experimental

Experimental code generation and transformation system.

**Features:**
- Template-based code generation
- Multi-language output
- Pattern-driven transformation

---

### [JEFRY](./JEFRY)

**Type:** Utility Framework
**Language:** Mixed
**Status:** 🔬 Experimental

Experimental utility framework for rapid prototyping.

**Features:**
- Quick prototyping tools
- Utility generators
- Development helpers

---

### [4Di](./4Di)

**Type:** Language/Tool
**Language:** Mixed
**Status:** 🔬 Experimental

Four-dimensional code analysis and visualization experiment.

**Features:**
- Multi-dimensional code analysis
- Visualization experiments
- Novel representation methods

---

### [udl-directory-template](./udl-directory-template)

**Type:** Project Template
**Language:** N/A
**Status:** 🔬 Template

Template for creating new UDL projects with standardized structure.

**Contents:**
- Project structure templates
- Configuration templates
- Boilerplate code

## Development Guidelines

### Status Levels

- 🔬 **Experimental** - Active research, APIs may change
- 🚧 **Prototype** - Core concepts proven, needs refinement
- ⚡ **Fast-Moving** - Rapid iteration, frequent breaking changes
- 🎓 **Research** - Academic/research-focused
- 📦 **Incubating** - Stabilizing for potential graduation

### Working with Experimental Projects

```bash
# Navigate to experimental project
cd projects/experimental/project-name

# Most experimental projects are self-contained
# Check individual README for specific setup instructions

# General pattern for Python projects
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# General pattern for TypeScript projects
pnpm install
pnpm build
```

### Creating a New Experimental Project

```bash
# Use the template
cp -r udl-directory-template my-experiment
cd my-experiment

# Or create from scratch
mkdir my-experiment
cd my-experiment

# Initialize with basic structure
cat > README.md <<EOF
# My Experiment

**Status:** 🔬 Experimental
**Language:** [Your Language]
**Started:** $(date +%Y-%m)

## Purpose

Brief description of what you're exploring.

## Goals

- [ ] Goal 1
- [ ] Goal 2

## Current Status

What's working, what's not.

## Next Steps

What you plan to do next.
EOF
```

## Graduation Path

Experimental projects can graduate to stable categories when they meet these criteria:

### Requirements for Graduation

1. **Stability**
   - Consistent API for 3+ months
   - No major breaking changes planned
   - Core functionality complete

2. **Documentation**
   - Comprehensive README
   - API documentation
   - Usage examples
   - Architecture documentation

3. **Testing**
   - Test coverage >70%
   - Integration tests
   - CI/CD configured

4. **Quality**
   - Code review completed
   - Linting and formatting applied
   - Dependencies documented

### Graduation Process

1. Propose graduation in issue or discussion
2. Code review by maintainer
3. Documentation review
4. Testing verification
5. Move to appropriate category
6. Update all documentation

**Recent Graduations:** *(None yet - this category is new)*

## Research Areas

Current experimental focus areas:

### Language Design
- Novel syntax patterns
- DSL construction methodologies
- Parser generation techniques
- Language composition strategies

### Code Analysis
- Multi-dimensional code representation
- Performance analysis tools
- Pattern recognition
- Code transformation

### Development Tools
- Code generation systems
- Project templating
- Rapid prototyping frameworks
- Development utilities

## Contributing

Experimental projects have more relaxed contribution requirements:

- **Documentation** - Can be minimal, but should explain the concept
- **Tests** - Optional but encouraged
- **Breaking Changes** - Expected and acceptable
- **Iteration Speed** - Fast iteration encouraged
- **Exploration** - Try new ideas freely

However:
- Keep a README explaining what you're exploring
- Document interesting findings
- Share learnings with other projects
- Consider impact on other UDL projects

## Archiving Projects

Experimental projects may be archived if:
- Experiment concluded (successful or not)
- Concept disproven
- Superseded by better approach
- No activity for 12+ months

Archived projects move to `.archive/experimental/` with a summary of findings.

## Related Projects

- **[languages](../languages)** - Stable language implementations
- **[tools](../tools)** - Production-ready tools
- **[applications](../applications)** - Complete applications
- **[libraries](../libraries)** - Reusable components

## Resources

- [Language Design Patterns](../../docs/specs/)
- [DSL Construction Guide](../../docs/CONTRIBUTING.md)
- [Testing Standards](../../docs/specs/)

---

**Total Experimental Projects:** 9
**Active Experiments:** 9
**Status:** All experimental
**Last Updated:** December 2025

## Quick Reference

| Project | Type | Language | Focus Area |
|---------|------|----------|------------|
| mecha_development | Framework | Mixed | Language Development |
| mecha_lang | DSL | Mixed | Language Implementation |
| canon | Tool | Mixed | Language Canonicalization |
| PACER | Tool | Python | Performance Analysis |
| CLAY | Framework | Mixed | Language Composition |
| motleyBard | Tool | Python | Code Generation |
| JEFRY | Framework | Mixed | Rapid Prototyping |
| 4Di | Tool/Lang | Mixed | Multi-dimensional Analysis |
| udl-directory-template | Template | N/A | Project Scaffolding |

**Note:** All projects are experimental and subject to significant changes. Check individual project READMEs for current status.
