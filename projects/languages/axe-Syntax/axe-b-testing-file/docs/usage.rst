Usage
=====

Installation
----------------

To install `axe:Builder`, run:

.. code-block:: bash

    pip install axe_builder

## Building CLI Menus

Use the `build` command to create CLI templates from `axe:Syntax` strings.

Example
----------------

.. code-block:: bash

    axe-builder build "[M={2}]:[N+{3}]" --output my_cli.py

This command parses the syntax and exports the CLI template to `my_cli.py`.


Building a CLI Template
-----------------------

To build a CLI template from an **`axe:Syntax`** string, use the `build` command:

.. code-block:: bash

    axe-builder build "[M+{2}]:[N+{3}]" --output my_cli.py

This command parses the syntax, generates the CLI structure, and exports it to `my_cli.py`.

Launching the Textual TUI
-------------------------

For an interactive experience, launch the TUI using the `tui` command:

.. code-block:: bash

    axe-builder tui "[M+{2}]:[N+{3}]"

This opens a terminal-based interface where you can visualize and interact with your menu structure.

Parsing Syntax
--------------

To parse and view the structured commands without building a template, use the `parse` command:

.. code-block:: bash

    axe-builder parse "[M+{2}]:[N+{3}]"

This will display the parsed JSON representation of your syntax.