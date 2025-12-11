# tests/models/test_models.py

import pytest
from axe_builder.models.models import MenuCommand, SubCommand


def test_menu_command_validation():
    cmd = MenuCommand(type="M", operation="+", count=2)
    assert cmd.type == "M"
    assert cmd.operation == "+"
    assert cmd.count == 2

    with pytest.raises(ValueError):
        MenuCommand(type="X", operation="+", count=2)  # Invalid type


def test_sub_command_validation():
    subcmd = SubCommand(type="T", operation="=", value="Title")
    assert subcmd.type == "T"
    assert subcmd.operation == "="
    assert subcmd.value == "Title"

    with pytest.raises(ValueError):
        SubCommand(type="Y", operation="=", value="Invalid")  # Invalid type
