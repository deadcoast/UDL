# axe_builder/tui/tui.py

from pathlib import Path
from typing import List, Optional

from textual.app import App, ComposeResult
from textual.containers import Container, Grid
from textual.widgets import Header, Footer, Input, Static, Button, DataTable

from axe_builder.logger.logger import logger
from axe_builder.models.models import MenuCommand
from axe_builder.parser.parser import parse_axesyntax
from .widgets import MenuTree


class AxeBuilderTUI(App):
    """
    Textual UI Application for axe:Builder.

    Provides an interactive interface to parse, visualize, and export CLI menus defined using axe:Syntax.
    """

    CSS_PATH = "axe_builder/tui.css"
    BINDINGS = [
        ("ctrl+c", "quit", "Quit"),
        ("tab", "focus_next", "Focus Next"),
        ("shift+tab", "focus_previous", "Focus Previous"),
    ]

    def __init__(self, syntax: str, **kwargs):
        """
        Initializes the AxeBuilderTUI application.

        Args:
            syntax (str): The axe:Syntax string to visualize and interact with.
        """
        super().__init__(**kwargs)
        self.syntax = syntax
        self.parsed_commands: List[MenuCommand] = []
        self.export_path: str = "cli_template.py"

    def on_load(self) -> None:
        """Bind keys for the application."""
        for key, action, description in self.BINDINGS:
            self.bind(key, action, description)

    def on_mount(self) -> None:
        """Set up the layout and widgets."""
        grid = Grid()
        grid.add_column("left", fraction=3)
        grid.add_column("right", fraction=2)

        grid.add_row("header", fraction=1)
        grid.add_row("main", fraction=8)
        grid.add_row("footer", fraction=1)

        self.header = Header()
        self.footer = Footer()
        self.menu_tree = MenuTree("Menu Commands", self.parsed_commands)
        self.input_field = Input(placeholder="Enter axe:Syntax here...", name="syntax_input")
        self.parse_button = Button(label="Parse Syntax", name="parse_button")
        self.export_button = Button(label="Export CLI", name="export_button")
        self.status = Static("Status: Waiting for input...", name="status")
        self.error_message = Static("", name="error_message")
        self.menu_tree = MenuTree("Menu Commands", self.parsed_commands)
        self.log_view = DataTable(title="Logs", name="log_view")

        grid.place(
            self.header,
            self.menu_tree,
            Container(
                self.input_field,
                self.parse_button,
                self.export_button,
                self.status,
                self.error_message,
                self.log_view,
                id="right_container"
            ),
            self.footer
        )

        self.view.dock(grid)

    def compose(self) -> ComposeResult:
        """Compose the UI components."""
        yield self.header
        yield self.menu_tree
        yield Container(
            self.input_field,
            self.parse_button,
            self.export_button,
            self.status,
            self.error_message,
            self.log_view,
            id="right_container"
        )
        yield self.footer

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "parse_button":
            await self.parse_syntax()
        elif event.button.id == "export_button":
            await self.export_cli()

    async def parse_syntax(self) -> None:
        """Parse the axe:Syntax input and update the menu tree."""
        syntax = self.input_field.value.strip()
        self.status.update("Status: Parsing...")
        self.error_message.update("")
        self.log_view.clear_rows()

        if not syntax:
            self.error_message.update("Error: Syntax input is empty.")
            self.status.update("Status: Parsing failed.")
            return

        try:
            logger.info("Parsing syntax from TUI input")
            self.parsed_commands = parse_axesyntax(syntax)
            self.menu_tree.update_menu_commands(self.parsed_commands)
            self.status.update("Status: Parsing successful!")
            logger.success("Syntax parsed and tree updated")
            await self.display_logs()
        except Exception as e:
            logger.error(f"TUI Parsing failed: {e}")
            self.error_message.update(f"Error: {e}")
            self.status.update("Status: Parsing failed.")
            await self.display_logs()

    async def export_cli(self) -> None:
        """Export the parsed commands to a Python CLI template."""
        if not self.parsed_commands:
            self.error_message.update("Error: No parsed commands to export.")
            self.status.update("Status: Export failed.")
            return

        try:
            logger.info(f"Exporting CLI template to {self.export_path}")
            from axe_builder.exporter.exporter import export_cli_template
            export_cli_template(self.parsed_commands, self.export_path)
            self.status.update(f"Status: CLI template exported to {self.export_path}")
            logger.success("CLI template exported successfully")
            await self.display_logs()
        except Exception as e:
            logger.error(f"Export failed: {e}")
            self.error_message.update(f"Error: {e}")
            self.status.update("Status: Export failed.")
            await self.display_logs()

    async def display_logs(self) -> None:
        """Display recent log entries in the log view."""
        try:
            log_file = Path("axe_builder.log")
            if log_file.exists():
                logs = log_file.read_text(encoding='utf-8').splitlines()
                recent_logs = logs[-10:]
                for log_entry in recent_logs:
                    self.log_view.add_row(log_entry)
        except Exception as e:
            logger.error(f"Failed to display logs: {e}")
            self.error_message.update(f"Error displaying logs: {e}")


def launch_tui(syntax: str):
    """
    Launches the Textual UI application.

    Args:
        syntax (str): The axe:Syntax string to visualize and interact with.
    """
    app = AxeBuilderTUI(syntax=syntax)
    app.run()
