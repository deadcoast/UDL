# tests/cli/test_cli.py

from typer.testing import CliRunner
from axe_builder.cli import app
from unittest.mock import patch

runner = CliRunner()

def test_parse_command_success():
    syntax = "[M+{2}]:[N+{3}]"
    result = runner.invoke(app, ["parse-command", syntax])
    assert result.exit_code == 0
    assert '"type": "M"' in result.stdout
    assert '"operation": "' in result.stdout
    assert '"count": 2' in result.stdout

def test_parse_command_failure():
    syntax = "[X+{2}]"
    result = runner.invoke(app, ["parse-command", syntax])
    assert result.exit_code != 0
    assert "Error" in result.stderr

def test_build_command_success():
    syntax = "[M={1}]:[N+{2}]"
    output = "test_cli.py"
    with patch("axe_builder.exporter.exporter.export_cli_template") as mock_export:
        result = runner.invoke(app, ["build", syntax, "--output", output])
        assert result.exit_code == 0
        assert f"CLI template exported to {output}" in result.stdout
        mock_export.assert_called_once()

def test_build_command_failure():
    syntax = "[M+{-1}]"
    output = "test_cli.py"
    result = runner.invoke(app, ["build", syntax, "--output", output])
    assert result.exit_code != 0
    assert "Error" in result.stderr

def test_tui_command():
    syntax = "[M+{1}]:[N+{2}]"
    result = runner.invoke(app, ["tui", syntax])
    # TUI launches an interactive interface; basic test to check exit code
    assert result.exit_code == 0
