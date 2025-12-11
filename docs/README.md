# UDL Documentation

**Purpose:** Comprehensive documentation for the UDL monorepo
**Audience:** Developers, AI assistants, contributors
**Status:** Active Maintenance

## Overview

This directory contains all extended documentation for the UDL (Universal Development Languages) monorepo, including architecture guides, migration documentation, specifications, and project-specific guides.

## Documentation Index

### Core Documentation

#### [MONOREPO-STATUS.md](./MONOREPO-STATUS.md)
**Current state of the monorepo**
- Recent updates and changes
- Build system status
- Known issues and limitations
- Project statistics
- Quick reference guide

**When to read:** To understand the current state of the monorepo

---

#### [MONOREPO_ARCHITECTURE.md](./MONOREPO_ARCHITECTURE.md)
**Architecture design and technical decisions**
- Technology stack
- Directory structure
- Workspace configuration
- CI/CD strategy
- Versioning approach
- Cross-project dependencies

**When to read:** Planning new features or understanding the system design

---

#### [MIGRATION_SUCCESS.md](./MIGRATION_SUCCESS.md)
**Migration completion summary**
- What was accomplished
- Infrastructure created
- Migration statistics
- Lessons learned
- Before/after comparison

**When to read:** Understanding how we got here and what changed

---

#### [MIGRATION_PLAN.md](./MIGRATION_PLAN.md)
**Original migration strategy**
- Migration phases
- Tooling choices
- Risk mitigation
- Historical context

**When to read:** Understanding the planning behind the migration

## Directory Structure

```
docs/
├── README.md                    # This file
├── MONOREPO-STATUS.md          # Current status
├── MONOREPO_ARCHITECTURE.md    # Architecture docs
├── MIGRATION_SUCCESS.md        # Migration summary
├── MIGRATION_PLAN.md           # Migration strategy
├── projects/                   # Project-specific docs
│   └── (project documentation index)
└── specs/                      # Specifications
    └── (technical specifications)
```

## Documentation Categories

### Architecture & Design
- System architecture
- Design patterns
- Technical decisions (ADRs)
- Integration strategies

### Guides & Tutorials
- Getting started
- Development workflows
- Best practices
- Common patterns

### Specifications
- Language specifications
- API specifications
- Protocol definitions
- Format specifications

### Project Documentation
- Individual project docs
- Cross-project guides
- Integration examples

## Documentation Standards

### Markdown Format

All documentation uses GitHub-Flavored Markdown:

```markdown
# Title (H1 - One per document)

## Section (H2)

### Subsection (H3)

**Bold** for emphasis
*Italic* for terminology
`code` for inline code

```language
# Code blocks with language tags
```

- Bullet lists
1. Numbered lists

[Links](./relative/path.md)
```

### File Naming

- `ALLCAPS.md` - Major documentation files
- `kebab-case.md` - General documentation
- `PascalCase.md` - Specification documents

### Document Structure

Each document should include:

1. **Title** - Clear, descriptive
2. **Metadata** - Purpose, audience, status
3. **Overview** - Brief description
4. **Table of Contents** - For long documents
5. **Main Content** - Well-organized sections
6. **Related Links** - Cross-references
7. **Footer** - Maintenance info

### Example Template

```markdown
# Document Title

**Purpose:** What this document covers
**Audience:** Who should read this
**Status:** Current status (Draft, Active, Deprecated)

## Overview

Brief description of what this document contains.

## Table of Contents

- [Section 1](#section-1)
- [Section 2](#section-2)

## Section 1

Content here...

## Section 2

More content...

## Related Documentation

- [Related Doc 1](./path/to/doc1.md)
- [Related Doc 2](./path/to/doc2.md)

---

**Last Updated:** YYYY-MM-DD
**Maintained By:** Maintainer name
**Version:** X.Y.Z
```

## Contributing Documentation

### Adding New Documentation

1. **Choose location:**
   - Root docs/ - Major monorepo docs
   - projects/ - Project-specific docs
   - specs/ - Technical specifications

2. **Create file:**
   ```bash
   cd docs
   touch my-new-doc.md
   ```

3. **Follow template:**
   - Use standard structure
   - Include metadata
   - Add to index

4. **Link it:**
   - Update this README
   - Add cross-references
   - Link from related docs

### Updating Existing Documentation

1. **Check currency:**
   - Is information still accurate?
   - Are examples up to date?
   - Do links still work?

2. **Make changes:**
   - Update content
   - Fix broken links
   - Add clarifications

3. **Update metadata:**
   - Change "Last Updated" date
   - Bump version if major changes
   - Add to changelog (if exists)

### Documentation Review

Before committing documentation:

- [ ] Spelling and grammar checked
- [ ] Links tested and working
- [ ] Code examples verified
- [ ] Markdown linting passed
- [ ] Cross-references added
- [ ] Index updated

## Markdown Linting

Documentation uses markdownlint for consistency:

```bash
# Install markdownlint
npm install -g markdownlint-cli2

# Check documentation
markdownlint-cli2 "docs/**/*.md"

# Auto-fix issues
markdownlint-cli2 --fix "docs/**/*.md"
```

Configuration: `.markdownlint.json` (root)

## Documentation Tools

### Recommended Tools

- **VSCode Extensions:**
  - Markdown All in One
  - markdownlint
  - Markdown Preview Enhanced

- **Linters:**
  - markdownlint-cli2
  - remark-lint

- **Generators:**
  - markdown-toc (table of contents)
  - jsdoc2md (API docs from code)

### Viewing Documentation

```bash
# Local preview
npx markdown-server docs/

# Or use VSCode preview (Cmd+Shift+V)

# Generate HTML
npx markdown-it docs/README.md > docs/README.html
```

## Organization Principles

### Single Source of Truth

Each topic should have one authoritative document:
- No duplicate information
- Cross-link related topics
- Update in one place

### Layered Information

Organize from high-level to detailed:
1. **Overview** - What and why
2. **Quickstart** - How to get started
3. **Reference** - Detailed information
4. **Examples** - Practical usage

### Progressive Disclosure

Start simple, add complexity:
- Basic concepts first
- Advanced topics later
- Optional details in appendices

## Special Documentation Types

### Architecture Decision Records (ADRs)

```markdown
# ADR-001: Use TurboRepo for Build Orchestration

**Date:** 2025-12-10
**Status:** Accepted

## Context
We need to build 33 projects efficiently...

## Decision
We will use TurboRepo because...

## Consequences
- Positive: Fast builds, caching
- Negative: Learning curve
```

### Specifications

```markdown
# CTX-CARD Format Specification

**Version:** 2.0
**Status:** Stable

## Abstract
CTX-CARD is a token-efficient format...

## Notation
Tags use prefix-free encoding...
```

## Maintenance

### Regular Tasks

- **Weekly:**
  - Fix broken links
  - Update outdated examples

- **Monthly:**
  - Review recent changes
  - Update getting started guide
  - Check for documentation gaps

- **Quarterly:**
  - Major documentation review
  - Reorganize if needed
  - Update architecture docs

### Deprecation

When deprecating documentation:

1. Add deprecation notice at top
2. Link to replacement
3. Keep for reference (don't delete)
4. Move to `.archive/docs/` after 6 months

## Future Plans

- [ ] Add tutorial series
- [ ] Create video walkthroughs
- [ ] Build searchable docs site
- [ ] Add interactive examples
- [ ] Generate API documentation from code
- [ ] Create architecture diagrams
- [ ] Add troubleshooting guides

## Related Resources

### External Links

- [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/)
- [markdownlint Rules](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md)
- [Documentation System](https://documentation.divio.com/)

### Internal Links

- [Root README](../README.md)
- [CLAUDE.md](../CLAUDE.md)
- [Project READMEs](../projects/)

---

**Total Documents:** 4 major docs + project/spec docs
**Format:** GitHub-Flavored Markdown
**Linting:** markdownlint-cli2
**Last Major Update:** December 2025
**Maintained By:** UDL Team
