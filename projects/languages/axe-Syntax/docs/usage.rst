Usage
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
