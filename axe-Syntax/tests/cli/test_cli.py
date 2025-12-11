from typer.testing import CliRunner
from axe_syntax.axe_builder import app

runner = CliRunner()

def test_parse_command():
    syntax = "[M+{2}]"
    result = runner.invoke(app, ["parse-command", syntax])
    assert result.exit_code == 0
    assert '"type": "M"' in result.stdout

def test_build_command():
    syntax = "[M={1}]"
    output = "test_cli.py"
    result = runner.invoke(app, ["build", syntax, "--output", output])
    assert result.exit_code == 0
    assert f"CLI template exported to {output}" in result.stdout

def test_tui_command():
    syntax = "[M={1}]:[N+{2}]"
    result = runner.invoke(app, ["tui", syntax])
    # TUI launches an interactive interface; basic test to check exit code
    assert result.exit_code == 0
