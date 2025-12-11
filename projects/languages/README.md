# Languages

Domain-Specific Languages (DSLs) and language implementations.

## Projects

### Production-Ready

- **[gate](gate/)** - Pattern language with LSP support and VSCode extension
- **[f8Syntax](f8Syntax/)** - F8 language system with execution engine and metrics
- **[DrRx](DrRx/)** - Schema-based DSL with validation

### Active Development

- **[axe-Syntax](axe-Syntax/)** - CLI menu builder using axe:Syntax notation with Textual TUI
- **[1az](1az/)** - VSCode extension for .1az language support
- **[gateppattern-1.1](gateppattern-1.1/)** - Enhanced gate pattern language implementation
- **[remedysyntax](remedysyntax/)** - Remedy language syntax support
- **[hoc](hoc/)** - High-order calculator language

## Common Patterns

All language projects follow similar structures:
- **Parser/Lexer** - Grammar definition and tokenization
- **AST** - Abstract syntax tree representation
- **LSP Server** (where applicable) - Language Server Protocol implementation
- **VSCode Extension** (where applicable) - Editor integration
- **Tests** - Comprehensive test suites

## Development

```bash
# TypeScript-based languages
cd projects/languages/gate
pnpm install
pnpm dev

# Python-based languages
cd projects/languages/axe-Syntax
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Contributing

When adding a new language:
1. Create directory in `projects/languages/`
2. Follow existing project structure
3. Add LSP support if applicable
4. Include comprehensive examples
5. Write tests for all language features
