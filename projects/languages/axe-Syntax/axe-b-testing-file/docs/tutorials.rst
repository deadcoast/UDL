Tutorials
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

       axe-builder build "[M={1}]:[N+(T="Nested Menu 1 Title")={2}]" --output enhanced_cli.py

3. **Run the Generated CLI**:

   .. code-block:: bash

       python enhanced_cli.py M1
       python enhanced_cli.py N1_1
       python enhanced_cli.py N1_2
   