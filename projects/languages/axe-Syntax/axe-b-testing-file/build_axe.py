from pathlib import Path

# Define the project structure with directories and files
project_structure = {
    "axe_builder/": {
        "__init__.py": "",
        "cli.py": '''import typer
from axe_builder.parser.parser import parse_axesyntax
from axe_builder.exporter.exporter import export_cli_template
from axe_builder.logger.logger import logger
from axe_builder.tui.tui import launch_tui

app = typer.Typer(help="axe:Builder - A CLI Menu Builder using axe:Syntax")

@app.command()
def parse_command(syntax: str):
    """
    Parse an axe:Syntax string and display the structured commands.
    """
    try:
        logger.info("Parsing axe:Syntax input")
        parsed_commands = parse_axesyntax(syntax)
        for cmd in parsed_commands:
            typer.echo(cmd.json(indent=4))
    except Exception as e:
        logger.error(f"Parsing failed: {e}")
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)

@app.command()
def build(syntax: str, output: str = "cli_template.py"):
    """
    Build CLI menus from axe:Syntax and export to a Python CLI template.
    """
    try:
        logger.info(f"Building CLI template from syntax: {syntax}")
        parsed_commands = parse_axesyntax(syntax)
        export_cli_template(parsed_commands, output)
        typer.echo(f"CLI template exported to {output}")
    except Exception as e:
        logger.error(f"Build failed: {e}")
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)

@app.command()
def tui(syntax: str):
    """
    Launch the Textual UI to interact with the defined CLI menus.
    """
    try:
        logger.info("Launching Textual TUI")
        launch_tui(syntax)
    except Exception as e:
        logger.error(f"TUI launch failed: {e}")
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
''',
        "parser/": {
            "__init__.py": "",
            "parser.py": '''from lark import Lark, Transformer, UnexpectedInput
from axe_builder.parser.transformer import AxeSyntaxTransformer
from axe_builder.logger.logger import logger
from pathlib import Path

# Load the grammar from axe_syntax.lark
grammar_path = Path(__file__).parent / "axe_syntax.lark"
with grammar_path.open() as f:
    axe_syntax_grammar = f.read()

# Initialize the Lark parser
parser = Lark(
    axe_syntax_grammar,
    start='start',
    parser='lalr',  # LALR(1) parser for efficiency
    propagate_positions=True,
    maybe_placeholders=False
)

def parse_axesyntax(syntax_str: str):
    """
    Parses an axe:Syntax string and returns a list of MenuCommand objects.

    Args:
        syntax_str (str): The axe:Syntax string to parse.

    Returns:
        List[MenuCommand]: Parsed MenuCommand objects.

    Raises:
        ValueError: If the syntax is invalid.
        RuntimeError: For unexpected parsing errors.
    """
    try:
        logger.bind(syntax=syntax_str).info("Starting parsing of axe:Syntax")
        parse_tree = parser.parse(syntax_str)
        transformer = AxeSyntaxTransformer()
        result = transformer.transform(parse_tree)
        logger.bind(syntax=syntax_str).success("Parsing completed successfully")
        return result
    except UnexpectedInput as e:
        logger.bind(syntax=syntax_str).error(f"Syntax Error: {e}")
        raise ValueError(f"Invalid axe:Syntax input. {e}")
    except Exception as e:
        logger.bind(syntax=syntax_str).exception("Unexpected parsing error")
        raise RuntimeError(f"An unexpected error occurred during parsing: {e}")
''',
            "axe_syntax.lark": """# axe_syntax.lark
# Lark grammar for axe:Syntax

%import common.ESCAPED_STRING
%import common.NUMBER
%import common.WS
%ignore WS  # Ignore whitespace

start: command_line

command_line: command (":" command)?

command: menu_command | sub_command

menu_command: "[" MENU_TYPE (operator operand)* "]"

sub_command: "(" SUB_TYPE (operator operand)* ")"

operator: "+" | "="

operand: sub_command | NUM_VAR | value

MENU_TYPE: "M" | "N"

SUB_TYPE: "T" | "."

NUM_VAR: "{" NUMBER "}"

value: ESCAPED_STRING
""",
            "transformer.py": """from lark import Transformer
from typing import List, Optional
from axe_builder.models.models import MenuCommand, SubCommand
from loguru import logger

class AxeSyntaxTransformer(Transformer):
    def start(self, items):
        logger.debug(f"Transforming start with items: {items}")
        return items

    def command_line(self, items):
        logger.debug(f"Transforming command_line with items: {items}")
        return items

    def command(self, items):
        logger.debug(f"Transforming command with items: {items}")
        return items[0]

    def menu_command(self, items):
        menu_type = items[0]
        operation = None
        count = None
        subcommands = []
        for i in range(1, len(items), 2):
            op = items[i]
            operand = items[i+1]
            if isinstance(operand, SubCommand):
                subcommands.append(operand)
            elif isinstance(operand, int):
                if op == "+":
                    count = operand
                    operation = op
                elif op == "=":
                    count = operand
                    operation = op
        logger.debug(f"Creating MenuCommand: type={menu_type}, operation={operation}, count={count}, subcommands={subcommands}")
        return MenuCommand(type=menu_type, operation=operation, count=count, subcommands=subcommands)

    def sub_command(self, items):
        sub_type = items[0]
        operation = None
        value = None
        count = None
        for i in range(1, len(items), 2):
            op = items[i]
            operand = items[i+1]
            if op == "=":
                if isinstance(operand, int):
                    count = operand
                elif isinstance(operand, str):
                    value = operand
                operation = op
            elif op == "+":
                operation = op
                # Handle addition if needed
        logger.debug(f"Creating SubCommand: type={sub_type}, operation={operation}, value={value}, count={count}")
        return SubCommand(type=sub_type, operation=operation, value=value, count=count)

    def operator(self, items):
        return items[0]

    def operand(self, items):
        return items[0]

    def MENU_TYPE(self, token):
        return token.value

    def SUB_TYPE(self, token):
        return token.value

    def NUM_VAR(self, token):
        return int(token.value.strip("{}"))

    def value(self, token):
        return token.value.strip('"')
""",
        },
        "models/": {
            "__init__.py": "",
            "models.py": """from pydantic import BaseModel, Field, validator
from typing import List, Optional

class SubCommand(BaseModel):
    type: str  # "T" for Title, "." for Custom
    operation: Optional[str] = None  # "+" or "=" if applicable
    value: Optional[str] = None
    count: Optional[int] = None

    @validator('type')
    def validate_subcommand_type(cls, v):
        if v not in {"T", "."}:
            raise ValueError("Invalid SubCommand type. Must be 'T' or '.'")
        return v

class MenuCommand(BaseModel):
    type: str  # "M" for Main Menu, "N" for Nested Menu
    operation: Optional[str] = None  # "+" or "="
    count: Optional[int] = None
    subcommands: List[SubCommand] = Field(default_factory=list)

    @validator('type')
    def validate_menu_type(cls, v):
        if v not in {"M", "N"}:
            raise ValueError("Invalid MenuCommand type. Must be 'M' or 'N'")
        return v

    @validator('operation')
    def validate_operation(cls, v):
        if v and v not in {"+", "="}:
            raise ValueError("Invalid operation. Must be '+' or '='")
        return v

    @validator('count')
    def validate_count(cls, v):
        if v is not None and v <= 0:
            raise ValueError("Count must be a positive integer")
        return v
""",
        },
        "tui/": {
            "__init__.py": "",
            "tui.py": """from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, ListView, ListItem, Static, Input
from axe_builder.parser.parser import parse_axesyntax
from axe_builder.models.models import MenuCommand, SubCommand
from axe_builder.logger.logger import logger
from .widgets import MenuTree
from typing import List

class AxeBuilderTUI(App):
    CSS_PATH = "axe_builder/tui.css"

    def __init__(self, syntax: str, **kwargs):
        super().__init__(**kwargs)
        self.syntax = syntax
        self.parsed_commands: List[MenuCommand] = []

    def on_mount(self) -> None:
        self.header = Header()
        self.footer = Footer()
        self.menu_tree = MenuTree("Menu Commands", self.parsed_commands)
        self.input_field = Input(placeholder="Enter axe:Syntax here...", name="syntax_input")
        self.submit_button = Static("[bold green]Press Enter to Parse[/bold green]")
        self.status = Static("Status: Waiting for input...", name="status")

        self.main_container = self.view.dock(self.header, edge="top")
        self.view.dock(self.footer, edge="bottom")
        self.view.dock(self.menu_tree, edge="left", size=60)
        self.view.dock(
            self.input_field,
            edge="bottom",
            size=3,
            name="input_section"
        )
        self.view.dock(self.status, edge="bottom", size=1)

    def compose(self) -> ComposeResult:
        yield self.header
        yield self.menu_tree
        yield self.input_field
        yield self.submit_button
        yield self.status
        yield self.footer

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        syntax = event.value
        self.status.update("Status: Parsing...")
        try:
            logger.info("Parsing syntax from TUI input")
            self.parsed_commands = parse_axesyntax(syntax)
            self.menu_tree.update_menu_commands(self.parsed_commands)
            self.status.update("Status: Parsing successful!")
            logger.success("Syntax parsed and tree updated")
        except Exception as e:
            logger.error(f"TUI Parsing failed: {e}")
            self.status.update(f"Error: {e}")

def launch_tui(syntax: str):
    app = AxeBuilderTUI(syntax=syntax)
    app.run()
""",
            "widgets.py": """from textual.widgets import TreeControl, TreeNode
from textual.app import ComposeResult
from typing import List
from axe_builder.models.models import MenuCommand, SubCommand

class MenuTree(TreeControl):
    def __init__(self, title: str, parsed_commands: List[MenuCommand]):
        super().__init__(title, "menu")
        self.parsed_commands = parsed_commands
        self.populate_tree()

    def populate_tree(self):
        self.clear()
        for cmd in self.parsed_commands:
            node_label = f"{cmd.type} (Operation: {cmd.operation}, Count: {cmd.count})"
            node = self.add(node_label)
            for sub in cmd.subcommands:
                sub_label = f"  SubCommand: {sub.type} (Value: {sub.value})"
                self.add(sub_label, parent=node)

    def update_menu_commands(self, new_commands: List[MenuCommand]):
        self.parsed_commands = new_commands
        self.populate_tree()
""",
        },
        "exporter/": {
            "__init__.py": "",
            "exporter.py": '''from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path
from typing import List
from axe_builder.models.models import MenuCommand, SubCommand
from loguru import logger

def export_cli_template(menus: List[MenuCommand], output_path: str):
    """
    Exports the parsed axe:Syntax menus to a Python CLI template using Typer.

    Args:
        menus (List[MenuCommand]): The list of parsed MenuCommand objects.
        output_path (str): The file path to export the generated CLI template.
    """
    try:
        logger.info(f"Exporting CLI template to {output_path}")

        # Set up Jinja2 environment
        template_dir = Path(__file__).parent / "templates"
        env = Environment(
            loader=FileSystemLoader(searchpath=str(template_dir)),
            autoescape=select_autoescape(['jinja2'])
        )
        template = env.get_template("cli_template.jinja2")

        # Render the template with menus
        rendered = template.render(menus=menus)

        # Write the rendered template to the output file
        with open(output_path, "w") as f:
            f.write(rendered)

        logger.success(f"CLI template successfully exported to {output_path}")

    except Exception as e:
        logger.exception(f"Failed to export CLI template: {e}")
        raise
''',
            "templates/": {
                "cli_template.jinja2": '''# cli_template.py
import typer
from loguru import logger

app = typer.Typer()

@app.callback()
def main(
    ctx: typer.Context,
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose mode"),
):
    """
    axe:Builder CLI Application
    """
    if verbose:
        logger.add("cli_verbose.log", level="DEBUG")
        logger.debug("Verbose mode enabled")

{% for menu in menus %}
@app.command(name="{{ menu.type }}{{ menu.count if menu.count else '' }}", help="Generated {{ menu.type }} Menu")
def {{ menu.type.lower() }}{{ menu.count if menu.count else '' }}():
    """
    {{ menu.type }} Menu Handler
    """
    try:
        logger.info("Executing {{ menu.type }}{{ menu.count if menu.count else '' }} Menu")
        typer.echo("This is {{ menu.type }}{{ ' ' + str(menu.count) if menu.count else '' }} Menu")
    except Exception as e:
        logger.error(f"Error in {{ menu.type }} Menu: {e}")
        typer.echo(f"An error occurred: {e}", err=True)

    {% for idx, sub in enumerate(menu.subcommands, start=1) %}
    @app.command(name="{{ sub.type }}{{ sub.count if sub.count else '' }}_{{ idx }}", help="Generated {{ sub.type }} SubCommand")
    def {{ sub.type.lower() }}{{ sub.count if sub.count else '' }}_{{ idx }}():
        """
        {{ sub.type }} SubCommand Handler
        """
        try:
            logger.info("Executing {{ sub.type }} SubCommand")
            {% if sub.value %}
            typer.echo("{{ sub.value }}")
            {% else %}
            typer.echo("This is a custom subcommand.")
            {% endif %}
        except Exception as e:
            logger.error(f"Error in {{ sub.type }} SubCommand: {e}")
            typer.echo(f"An error occurred: {e}", err=True)
    {% endfor %}

{% endfor %}

if __name__ == "__main__":
    app()
''',
            },
        },
        "logger/": {
            "__init__.py": "",
            "logger.py": """from loguru import logger
import sys

# Remove default logger
logger.remove()

# Console sink with colored output and INFO level
logger.add(
    sys.stderr,
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>",
    enqueue=True
)

# File sink with rotation and DEBUG level
logger.add(
    "axe_builder.log",
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}",
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    enqueue=True,
    serialize=False
)

# JSON sink for structured logging
logger.add(
    "axe_builder.json",
    level="DEBUG",
    format="{\"time\": \"{time:YYYY-MM-DD HH:mm:ss}\", \"level\": \"{level}\", \"message\": \"{message}\"}",
    rotation="50 MB",
    retention="30 days",
    compression="gzip",
    enqueue=True,
    serialize=True
)
""",
        },
        "utils/": {
            "__init__.py": "",
            "utils.py": '''# utils.py
# Utility functions for axe:Builder

def validate_syntax(syntax: str) -> bool:
    """
    Validates the axe:Syntax string format.

    Args:
        syntax (str): The axe:Syntax string to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    # Placeholder for actual validation logic
    return True
''',
        },
        "config/": {
            "__init__.py": "",
            "settings.py": """# settings.py
# Configuration settings for axe:Builder

DEFAULT_OUTPUT_PATH = "cli_template.py"
LOG_FILE = "axe_builder.log"
JSON_LOG_FILE = "axe_builder.json"
VERBOSE_MODE = False
""",
        },
    },
    "tests/": {
        "__init__.py": "",
        "parser/": {
            "__init__.py": "",
            "test_parser.py": """import pytest
from axe_builder.parser.parser import parse_axesyntax
from axe_builder.models.models import MenuCommand, SubCommand

def test_parse_multiple_main_menus():
    syntax = "[M+{3}]"
    result = parse_axesyntax(syntax)
    assert len(result) == 1
    cmd = result[0]
    assert isinstance(cmd, MenuCommand)
    assert cmd.type == "M"
    assert cmd.operation == "+"
    assert cmd.count == 3

def test_parse_nested_menus():
    syntax = "[M={2}]:[N+{3}]"
    result = parse_axesyntax(syntax)
    assert len(result) == 2
    main_menu, nested_menu = result
    assert isinstance(main_menu, MenuCommand)
    assert main_menu.type == "M"
    assert main_menu.operation == "="
    assert main_menu.count == 2
    assert isinstance(nested_menu, MenuCommand)
    assert nested_menu.type == "N"
    assert nested_menu.operation == "+"
    assert nested_menu.count == 3

def test_parse_title_subcommand():
    syntax = '[M={1}]:(T="Menu One Title")'
    result = parse_axesyntax(syntax)
    assert len(result) == 2
    main_menu, title_cmd = result
    assert isinstance(main_menu, MenuCommand)
    assert main_menu.type == "M"
    assert main_menu.count == 1
    assert isinstance(title_cmd, SubCommand)
    assert title_cmd.type == "T"
    assert title_cmd.value == "Menu One Title"
""",
        },
        "exporter/": {
            "__init__.py": "",
            "test_exporter.py": """from unittest.mock import mock_open, patch
from axe_builder.exporter.exporter import export_cli_template
from axe_builder.models.models import MenuCommand, SubCommand

def test_export_cli_template():
    parsed_commands = [
        MenuCommand(type="M", operation="+", count=2, subcommands=[
            SubCommand(type="T", operation="=", value="Main Menu Title"),
            SubCommand(type=".", operation="=", count=5)
        ]),
        MenuCommand(type="N", operation="+", count=3, subcommands=[
            SubCommand(type=".", operation="+", count=6)
        ])
    ]
    m = mock_open()
    with patch("builtins.open", m):
        export_cli_template(parsed_commands, "dummy_output.py")
        m.assert_called_once_with("dummy_output.py", "w")
        handle = m()
        handle.write.assert_called()  # Further assertions can be added
""",
        },
        "cli/": {
            "__init__.py": "",
            "test_cli.py": """from typer.testing import CliRunner
from axe_builder.cli import app

runner = CliRunner()

def test_parse_command():
    syntax = "[M+{2}]"
    result = runner.invoke(app, ["parse-command", syntax])
    assert result.exit_code == 0
    assert '"type": "M"' in result.stdout

def test_build_command():
    syntax = "[M={1}]"
    output = "test_cli.py"
    result = runner.invoke(app, ["build", syntax, "--output", output])
    assert result.exit_code == 0
    assert f"CLI template exported to {output}" in result.stdout

def test_tui_command():
    syntax = "[M={1}]:[N+{2}]"
    result = runner.invoke(app, ["tui", syntax])
    # TUI launches an interactive interface; basic test to check exit code
    assert result.exit_code == 0
""",
        },
        "tui/": {
            "__init__.py": "",
            "test_tui.py": """# Placeholder for TUI tests
# Testing TUI applications can be complex and may require specialized tools or manual testing
def test_tui_launch():
    # Example placeholder test
    assert True
""",
        },
        "logger/": {
            "__init__.py": "",
            "test_logger.py": """from axe_builder.logger.logger import logger

def test_logger_configuration():
    try:
        logger.info("Test logger info message")
        logger.debug("Test logger debug message")
        logger.error("Test logger error message")
        assert True
    except Exception:
        assert False
""",
        },
        "models/": {
            "__init__.py": "",
            "test_models.py": """from axe_builder.models.models import MenuCommand, SubCommand
import pytest

def test_menu_command_validation():
    cmd = MenuCommand(type="M", operation="+", count=2)
    assert cmd.type == "M"
    assert cmd.operation == "+"
    assert cmd.count == 2

    with pytest.raises(ValueError):
        MenuCommand(type="X", operation="+", count=2)  # Invalid type

def test_sub_command_validation():
    subcmd = SubCommand(type="T", operation="=", value="Title")
    assert subcmd.type == "T"
    assert subcmd.operation == "="
    assert subcmd.value == "Title"

    with pytest.raises(ValueError):
        SubCommand(type="Y", operation="=", value="Invalid")  # Invalid type
""",
        },
    },
    "examples/": {
        "example_a.axe": "[M={2}]:[N+{3}]",
        "example_b.axe": "[M={1}]:[N+(.)={6}]",
        "README.md": """# axe:Builder Examples

This directory contains example `axe:Syntax` files demonstrating how to define CLI menus using `axe:Builder`.

## Example A: Three Nested Menus in Main Menu #2

```plaintext
[M={2}]:[N+{3}]
```

## Example B: Six Nested Menus in Main Menu #1 with a Custom SubCommand

```plaintext
[M={1}]:[N+(.)={6}]
```
""",
    },
    "docs/": {
        "conf.py": """# conf.py
# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('../axe_builder'))

project = 'axe:Builder'
author = 'Your Name'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints'
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'furo'
html_static_path = ['_static']
""",
        "index.rst": """.. axe:Builder documentation master file, created by
   sphinx-quickstart on Tue Sep 28 10:00:00 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to axe:Builder's documentation!
========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage
   api
   tutorials

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
""",
        "usage.rst": """Usage
=====

## Installation

To install `axe:Builder`, run:

.. code-block:: bash

    pip install axe_builder

## Building CLI Menus

Use the `build` command to create CLI templates from `axe:Syntax` strings.

### Example

.. code-block:: bash

    axe-builder build "[M={2}]:[N+{3}]" --output my_cli.py

This command parses the syntax and exports the CLI template to `my_cli.py`.

## Launching the TUI

Use the `tui` command to launch the interactive Textual UI.

### Example

.. code-block:: bash

    axe-builder tui "[M={2}]:[N+{3}]"

This opens the TUI where you can visualize and interact with your menu structure.

## Parsing Syntax

Use the `parse-command` to parse and display the structured commands.

### Example

.. code-block:: bash

    axe-builder parse-command "[M={2}]:[N+{3}]"

This will output the JSON representation of the parsed commands.
""",
        "api.rst": """API Reference
=============

.. automodule:: axe_builder.cli
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: axe_builder.parser.parser
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: axe_builder.exporter.exporter
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: axe_builder.tui.tui
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: axe_builder.logger.logger
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: axe_builder.models.models
    :members:
    :undoc-members:
    :show-inheritance:
""",
        "tutorials.rst": """Tutorials
==========

## Creating a Simple CLI Menu

1. **Define the Syntax**:

   ```plaintext
   [M={1}]:[N+{2}]
   ```

2. **Build the CLI Template**:

   .. code-block:: bash

       axe-builder build "[M={1}]:[N+{2}]" --output simple_cli.py

3. **Run the Generated CLI**:

   .. code-block:: bash

       python simple_cli.py M1
       python simple_cli.py N1
       python simple_cli.py N2

## Adding Titles and Custom SubCommands

1. **Define the Enhanced Syntax**:

   ```plaintext
   [M={1}]:[N+(T="Nested Menu 1 Title")={2}]
   ```

2. **Build the CLI Template**:

   .. code-block:: bash

       axe-builder build "[M={1}]:[N+(T=\"Nested Menu 1 Title\")={2}]" --output enhanced_cli.py

3. **Run the Generated CLI**:

   .. code-block:: bash

       python enhanced_cli.py M1
       python enhanced_cli.py N1_1
       python enhanced_cli.py N1_2
   """,
    },
    "_static/": {
        "axe_builder/": {
            "tui.css": """/* tui.css */
/* Custom CSS for Textual TUI */

Header {
    background: #4F5D75;
    color: white;
    padding: 1;
}

Footer {
    background: #4F5D75;
    color: white;
    padding: 1;
}

ListView {
    background: #354F52;
    color: white;
}

ListItem {
    padding: 0.5 1;
}

Input {
    background: #CAD2C5;
    color: black;
}

Static#status {
    background: #CAD2C5;
    color: black;
}

Static#parse-button {
    color: green;
    bold: true;
}
"""
        }
    },
    ".github/": {
        "workflows/": {
            "ci.yml": """name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Lint with flake8
      run: |
        pip install flake8
        flake8 axe_builder tests
    - name: Run Tests
      run: |
        pip install pytest hypothesis
        pytest
    - name: Build Documentation
      run: |
        pip install sphinx
        cd docs
        make html
    - name: Upload Documentation
      uses: actions/upload-artifact@v2
      with:
        name: documentation
        path: docs/_build/html
"""
        }
    },
    "requirements.txt": """typer==0.9.0
lark-parser==1.1.5
textual==0.2.1
loguru==0.6.0
pydantic==1.10.2
pytest==7.1.2
hypothesis==6.52.2
jinja2==3.1.2
sphinx==4.5.0
sphinx-autodoc-typehints==1.19.2
""",
    "pyproject.toml": """[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "axe_builder"
version = "0.1.0"
description = "A CLI Menu Builder using axe:Syntax"
authors = [
    { name="Your Name", email="you@example.com" }
]
dependencies = [
    "typer==0.9.0",
    "lark-parser==1.1.5",
    "textual==0.2.1",
    "loguru==0.6.0",
    "pydantic==1.10.2",
    "pytest==7.1.2",
    "hypothesis==6.52.2",
    "jinja2==3.1.2",
    "sphinx==4.5.0",
    "sphinx-autodoc-typehints==1.19.2"
]

[project.scripts]
axe-builder = "axe_builder.cli:app"

[tool.setuptools.packages.find]
where = ["axe_builder"]
""",
    "README.md": """# axe:Builder

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
""",
    "setup.py": """from setuptools import setup, find_packages

setup(
    name="axe_builder",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer==0.9.0",
        "lark-parser==1.1.5",
        "textual==0.2.1",
        "loguru==0.6.0",
        "pydantic==1.10.2",
        "pytest==7.1.2",
        "hypothesis==6.52.2",
        "jinja2==3.1.2",
        "sphinx==4.5.0",
        "sphinx-autodoc-typehints==1.19.2"
    ],
    entry_points={
        "console_scripts": [
            "axe-builder=axe_builder.cli:app",
        ],
    },
    author="Your Name",
    author_email="you@example.com",
    description="A CLI Menu Builder using axe:Syntax",
    license="MIT",
    keywords="cli, typer, lark, textual, loguru",
    url="https://github.com/yourusername/axe_builder",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
""",
}


def create_structure(base_path: Path, structure: dict):
    for name, content in structure.items():
        path = base_path / name
        if isinstance(content, dict):
            path.mkdir(parents=True, exist_ok=True)
            create_structure(path, content)
        else:
            if not path.exists():
                path.parent.mkdir(parents=True, exist_ok=True)
                with path.open("w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Created file: {path}")
            else:
                print(f"File already exists: {path}")


def main():
    current_dir = Path.cwd()
    print(f"Creating axe_builder project in: {current_dir}")

    create_structure(current_dir, project_structure)

    print("\nProject structure created successfully!")


if __name__ == "__main__":
    main()
