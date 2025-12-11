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
        logger.info("Verbose mode enabled")

@app.command(name="M2", help="Generated M Menu")
def m2():
    """
    M Menu Handler
    """
    typer.echo("This is M 2 Menu")

    @app.command(name="N3_1", help="Generated N SubCommand")
    def n3_1():
        """
        N SubCommand Handler
        """
        typer.echo("This is a custom subcommand.")

    @app.command(name="N3_2", help="Generated N SubCommand")
    def n3_2():
        """
        N SubCommand Handler
        """
        typer.echo("This is a custom subcommand.")

    @app.command(name="N3_3", help="Generated N SubCommand")
    def n3_3():
        """
        N SubCommand Handler
        """
        typer.echo("This is a custom subcommand.")

@app.command(name="N3", help="Generated N Menu")
def n3():
    """
    N Menu Handler
    """
    typer.echo("This is N 3 Menu")

    @app.command(name="N3_1", help="Generated N SubCommand")
    def n3_1():
        """
        N SubCommand Handler
        """
        typer.echo("This is a custom subcommand.")

    @app.command(name="N3_2", help="Generated N SubCommand")
    def n3_2():
        """
        N SubCommand Handler
        """
        typer.echo("This is a custom subcommand.")

    @app.command(name="N3_3", help="Generated N SubCommand")
    def n3_3():
        """
        N SubCommand Handler
        """
        typer.echo("This is a custom subcommand.")

if __name__ == "__main__":
    app()