# UDL Extensions

Editor extensions and IDE plugins that provide language support, syntax highlighting, and enhanced editing capabilities for UDL languages and tools.

## Overview

This directory contains extensions for various text editors and IDEs, primarily focused on VSCode and Obsidian. These extensions integrate UDL's domain-specific languages into popular development environments, providing syntax highlighting, language servers, and specialized editing features.

## Projects in this Category

### [camo-obsidian](./camo-obsidian)

**Type:** Obsidian Plugin
**Language:** TypeScript
**Status:** ✅ Stable

Advanced camouflaged codeblocks plugin for Obsidian. Provides security-focused features for hiding and encrypting code snippets within markdown notes.

**Features:**
- Camouflaged code rendering
- Security integration
- Live preview compatibility
- Custom preset system
- Effect handlers for visual transformations

**Quick Start:**
```bash
cd camo-obsidian
pnpm install
pnpm build
```

**Documentation:** [camo-obsidian/README.md](./camo-obsidian/README.md)

## Development

### Building All Extensions

From the repository root:
```bash
# Build all extension projects
pnpm run build --filter="./projects/extensions/**"

# Test all extensions
pnpm run test --filter="./projects/extensions/**"
```

### Creating a New Extension

```bash
# Navigate to extensions directory
cd projects/extensions

# Create new extension project
mkdir my-extension
cd my-extension

# Initialize package.json
pnpm init
```

## Extension Types

### VSCode Extensions
Extensions for Visual Studio Code and compatible editors (Cursor, VSCodium, etc.).

**Packaging:**
```bash
vsce package
```

**Publishing:**
```bash
vsce publish
```

### Obsidian Plugins
Plugins for the Obsidian note-taking application.

**Structure:**
- `main.js` - Plugin entry point
- `manifest.json` - Plugin metadata
- `styles.css` - Custom styles

### Browser Extensions
(Future) Extensions for web browsers providing language support in online code editors.

## Common Technologies

- **TypeScript** - Primary development language
- **ESBuild** - Fast bundling
- **VSCode Extension API** - For VSCode extensions
- **Obsidian API** - For Obsidian plugins
- **Language Server Protocol (LSP)** - For language support

## Testing

Extensions should include:
- **Unit tests** - Test individual components
- **Integration tests** - Test extension activation and features
- **Manual testing** - Test in target environment

```bash
# Run tests for a specific extension
cd camo-obsidian
pnpm test
```

## Publishing

Each extension can be published independently to its respective marketplace:

- **VSCode:** Visual Studio Marketplace
- **Obsidian:** Obsidian Community Plugins
- **Browser Extensions:** Chrome Web Store, Firefox Add-ons

## Contributing

When adding a new extension:

1. Follow the directory structure of existing extensions
2. Include comprehensive README with installation instructions
3. Add tests for core functionality
4. Document all configuration options
5. Update this category README

## Related Projects

- **[languages](../languages)** - DSL implementations that extensions support
- **[tools](../tools)** - CLI tools that extensions may integrate with
- **[applications](../applications)** - Full applications that may use extensions

## Links

- [VSCode Extension API](https://code.visualstudio.com/api)
- [Obsidian Plugin Developer Docs](https://docs.obsidian.md/)
- [Language Server Protocol](https://microsoft.github.io/language-server-protocol/)

---

**Total Extensions:** 1
**Languages Supported:** TypeScript
**Target Editors:** Obsidian, (VSCode - future)
