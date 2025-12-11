# axe:Builder

**axe:Builder** is a Python-based CLI menu builder that utilizes a custom notation called **axe:Syntax** to define and generate hierarchical CLI menus.

## Features

- Define Main Menus, Nested Menus, and SubCommands using axe:Syntax.
- Interactive Textual TUI for visualizing and managing menus.
- Export menus to Python CLI templates using Typer.
- Comprehensive logging with Loguru.
- Modular and extensible architecture.

## Installation

To install `axe:Builder`, run:

```bash
pip install -r requirements.txt
```

## Usage

### Building CLI Menus

Use the `build` command to create CLI templates from `axe:Syntax` strings.

### Launching the TUI

Use the `tui` command to launch the interactive Textual UI.

### Parsing Syntax

Use the `parse-command` to parse and display the structured commands.

## Examples

Refer to the [examples](examples/README.md) directory for sample `axe:Syntax` files and their usage.

## Documentation

Comprehensive documentation is available in the [docs](docs/) directory.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before getting started.

## License

This project is licensed under the MIT License.
