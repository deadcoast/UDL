# tests/parser/test_parser.py

import pytest
from axe_builder.models.models import MenuCommand, SubCommand
from axe_builder.parser.parser import parse_axesyntax


def test_parse_multiple_main_menus():
    syntax = "[M+{3}]"
    result = parse_axesyntax(syntax)
    assert len(result) == 1
    cmd = result[0]
    assert isinstance(cmd, MenuCommand)
    assert cmd.type == "M"
    assert cmd.operation == "+"
    assert cmd.count == 3


def test_parse_nested_menus():
    syntax = "[M={2}]:[N+{3}]"
    result = parse_axesyntax(syntax)
    assert len(result) == 2
    main_menu, nested_menu = result
    assert isinstance(main_menu, MenuCommand)
    assert main_menu.type == "M"
    assert main_menu.operation == "="
    assert main_menu.count == 2
    assert isinstance(nested_menu, MenuCommand)
    assert nested_menu.type == "N"
    assert nested_menu.operation == "+"
    assert nested_menu.count == 3


def test_parse_title_subcommand():
    syntax = '[M={1}]:(T="Menu One Title")'
    result = parse_axesyntax(syntax)
    assert len(result) == 2
    main_menu, title_cmd = result
    assert isinstance(main_menu, MenuCommand)
    assert main_menu.type == "M"
    assert main_menu.count == 1
    assert isinstance(title_cmd, SubCommand)
    assert title_cmd.type == "T"
    assert title_cmd.value == "Menu One Title"


def test_parse_custom_subcommand_with_count():
    syntax = "[N+(.)={6}]"
    result = parse_axesyntax(syntax)
    assert len(result) == 1
    nested_menu = result[0]
    assert isinstance(nested_menu, MenuCommand)
    assert nested_menu.type == "N"
    assert nested_menu.operation == "+"
    assert nested_menu.count == 6
    assert len(nested_menu.subcommands) == 1
    subcmd = nested_menu.subcommands[0]
    assert isinstance(subcmd, SubCommand)
    assert subcmd.type == "."
    assert subcmd.count == 6
    assert subcmd.value is None
