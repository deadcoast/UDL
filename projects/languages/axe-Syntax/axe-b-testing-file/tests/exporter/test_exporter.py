# tests/exporter/test_exporter.py

from unittest.mock import mock_open, patch
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
        handle.write.assert_called()
