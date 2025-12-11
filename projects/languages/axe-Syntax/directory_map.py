from rich.tree import Tree
from rich.console import Console
import os

def build_tree(root_path, tree, ignore_dirs=None):
    """
    Recursively builds the tree structure starting from the root_path,
    excluding directories specified in ignore_dirs.

    Args:
        root_path (str): The root directory path.
        tree (Tree): The Rich Tree object to populate.
        ignore_dirs (set, optional): A set of directory names to ignore. Defaults to None.
    """
    if ignore_dirs is None:
        ignore_dirs = set()

    try:
        # Sort the items for consistent ordering
        for item in sorted(os.listdir(root_path)):
            item_path = os.path.join(root_path, item)
            # Check if the item is a directory and not in the ignore list
            if os.path.isdir(item_path):
                if item in ignore_dirs:
                    # Optionally, you can indicate that this directory is ignored
                    tree.add(f"[dim]{item}/ [italic](ignored)")
                    continue  # Skip adding this directory and its contents
                # Add the directory as a branch and recurse into it
                branch = tree.add(f"[bold blue]{item}/")
                build_tree(item_path, branch, ignore_dirs)
            else:
                # Add the file as a leaf node
                tree.add(item)
    except PermissionError:
        # Indicate that access to this directory is denied
        tree.add("[red]Permission Denied[/red]")

def export_tree_to_file(root_dir, output_file, ignore_dirs=None):
    """
    Creates a visual directory tree and exports it to a text file,
    excluding specified directories.

    Args:
        root_dir (str): The root directory to visualize.
        output_file (str): The path to the output text file.
        ignore_dirs (list, optional): A list of directory names to ignore. Defaults to None.
    """
    if ignore_dirs is None:
        ignore_dirs = []

    # Convert the ignore_dirs list to a set for faster lookup
    ignore_dirs_set = set(ignore_dirs)

    # Initialize the Rich Tree with the root directory name
    tree = Tree(f"[bold green]{os.path.basename(root_dir)}/")

    # Build the tree structure
    build_tree(root_dir, tree, ignore_dirs=ignore_dirs_set)

    # Initialize the Console with recording enabled
    console = Console(record=True, force_terminal=False)

    # Print the tree to the console (which is being recorded)
    console.print(tree)

    # Export the recorded content as plain text (without Rich's styling)
    tree_text = console.export_text()

    # Write the tree to the specified output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(tree_text)

    print(f"Directory tree has been exported to '{output_file}'.")

if __name__ == "__main__":
    # === Configuration ===

    # Specify the directory you want to visualize
    root_directory = "/Users/deadcoast/axe-Syntax"  # <-- Replace with your directory path

    # Specify the output file path
    output_text_file = os.path.join(root_directory, "directory_tree.txt")

    # Specify directories to ignore
    directories_to_ignore = [
        ".idea",
        ".mypy_cache",
        "__pycache__",
        ".git",
        "node_modules",
        ".venv",
        # Add more directory names you want to ignore here
    ]

    # === Execute ===
    export_tree_to_file(root_directory, output_text_file, ignore_dirs=directories_to_ignore)
