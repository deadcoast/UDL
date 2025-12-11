# axe_builder/exporter/exporter.py

from jinja2 import Environment, FileSystemLoader, select_autoescape
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
