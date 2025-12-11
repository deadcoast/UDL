# axe_builder/cli.py

import sys
from enum import Enum
from pathlib import Path
from typing import Optional

import typer
from axe_builder.exporter.exporter import export_cli_template
from axe_builder.logger.logger import logger
from axe_builder.parser.parser import AxeSyntaxParser
from axe_builder.tui.tui import launch_tui
from typer import Context

app = typer.Typer(help="axe:Builder - A CLI Menu Builder using axe:Syntax")


class OperationMode(str, Enum):
    parse = "parse"
    build = "build"
    tui = "tui"


@app.callback()
def main(
    ctx: Context,
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Enable verbose logging",
        show_default=False,
    ),
):
    """
    axe:Builder - A CLI Menu Builder using axe:Syntax
    """
    if verbose:
        logger.remove()
        logger.add(
            sys.stderr,
            level="DEBUG",
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>",
        )
        logger.debug("Verbose mode enabled")
    ctx.obj = {"verbose": verbose}


@app.command(
    name="parse",
    help="Parse an axe:Syntax string and display the structured commands.",
)
def parse_command(
    syntax: Optional[str] = typer.Argument(
        None, help="The axe:Syntax string to parse."
    ),
    file: Optional[Path] = typer.Option(
        None,
        "--file",
        "-f",
        help="Path to a file containing the axe:Syntax string.",
        exists=True,
        readable=True,
    ),
):
    """
    Parse an axe:Syntax string and display the structured commands.
    """
    try:
        if not syntax and not file:
            raise typer.BadParameter(
                "Either provide a syntax string or a file containing the syntax."
            )
        if file:
            syntax = file.read_text(encoding="utf-8").strip()
            logger.debug(f"Read syntax from file: {file}")
        logger.info("Parsing axe:Syntax input")
        parser = AxeSyntaxParser()
        parsed_commands = parser.parse(syntax)
        for cmd in parsed_commands:
            typer.echo(cmd.json(indent=4))
        logger.success("Parsing completed successfully.")
    except typer.BadParameter as e:
        logger.error(f"Bad parameter: {e}")
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1) from e
    except (ValueError, RuntimeError) as e:
        logger.error(f"Parsing failed: {e}")
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1) from e
    except Exception as e:
        logger.exception("An unexpected error occurred during parsing.")
        typer.echo(f"Unexpected Error: {e}", err=True)
        raise typer.Exit(code=1) from e


@app.command(
    name="build",
    help="Build CLI menus from axe:Syntax and export to a Python CLI template.",
)
def build_command(
    syntax: Optional[str] = typer.Argument(
        None, help="The axe:Syntax string to parse and build."
    ),
    file: Optional[Path] = typer.Option(
        None,
        "--file",
        "-f",
        help="Path to a file containing the axe:Syntax string.",
        exists=True,
        readable=True,
    ),
    output: Path = typer.Option(
        "cli_template.py",
        "--output",
        "-o",
        help="Path to export the generated CLI template.",
    ),
    overwrite: bool = typer.Option(
        False,
        "--overwrite",
        "-w",
        help="Overwrite the output file if it already exists.",
    ),
):
    """
    Build CLI menus from axe:Syntax and export to a Python CLI template.
    """
    try:
        if not syntax and not file:
            raise typer.BadParameter(
                "Either provide a syntax string or a file containing the syntax."
            )
        if file:
            syntax = file.read_text(encoding="utf-8").strip()
            logger.debug(f"Read syntax from file: {file}")
        if output.exists() and not overwrite:
            logger.error(
                f"Output file {output} already exists. Use --overwrite to overwrite."
            )
            typer.echo(
                f"Error: Output file {output} already exists. Use --overwrite to overwrite.",
                err=True,
            )
            raise typer.Exit(code=1)
        logger.info("Building CLI template from syntax")
        parser = AxeSyntaxParser()
        parsed_commands = parser.parse(syntax)
        export_cli_template(parsed_commands, str(output))
        logger.success(f"CLI template exported to {output}")
        typer.echo(f"CLI template exported to {output}")
    except typer.BadParameter as e:
        logger.error(f"Bad parameter: {e}")
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1) from e
    except (ValueError, RuntimeError) as e:
        logger.error(f"Build failed: {e}")
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1) from e
    except Exception as e:
        logger.exception("An unexpected error occurred during build.")
        typer.echo(f"Unexpected Error: {e}", err=True)
        raise typer.Exit(code=1) from e


@app.command(
    name="tui",
    help="Launch the Textual UI to interact with the defined CLI menus.",
)
def tui_command(
    syntax: Optional[str] = typer.Argument(
        None, help="The axe:Syntax string to parse and visualize."
    ),
    file: Optional[Path] = typer.Option(
        None,
        "--file",
        "-f",
        help="Path to a file containing the axe:Syntax string.",
        exists=True,
        readable=True,
    ),
):
    """
    Launch the Textual UI to interact with the defined CLI menus.
    """
    try:
        if not syntax and not file:
            raise typer.BadParameter(
                "Either provide a syntax string or a file containing the syntax."
            )
        if file:
            syntax = file.read_text(encoding="utf-8").strip()
            logger.debug(f"Read syntax from file: {file}")
        logger.info("Launching Textual TUI")
        launch_tui(syntax)
        logger.success("TUI launched successfully.")
    except typer.BadParameter as e:
        logger.error(f"Bad parameter: {e}")
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1) from e
    except Exception as e:
        logger.error(f"TUI launch failed: {e}")
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1) from e


if __name__ == "__main__":
    app()
