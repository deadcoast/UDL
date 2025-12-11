# axe_builder/tui/widgets.py

from typing import List

from axe_builder.models.models import MenuCommand, SubCommand
from loguru import logger
from textual.widgets import Tree


class MenuTree(Tree):
    def __init__(self, title: str, parsed_commands: List[MenuCommand]):
        super().__init__(title, "menu_tree")
        self.parsed_commands = parsed_commands
        self.populate_tree()

    def populate_tree(self):
        self.clear()
        for cmd in self.parsed_commands:
            node_label = f"{cmd.type} (Op: {cmd.operation}, Count: {cmd.count})"
            node = self.add(node_label)
            for sub in cmd.subcommands:
                if sub.type == "T":
                    sub_label = f"Title: {sub.value}"
                elif sub.type == ".":
                    sub_label = f"Custom Command (Count: {sub.count})"
                else:
                    sub_label = f"SubCommand: {sub.type}"
                self.add(sub_label, parent=node)
        logger.debug("Menu tree populated successfully.")

    def update_menu_commands(self, new_commands: List[MenuCommand]):
        self.parsed_commands = new_commands
        self.populate_tree()
        logger.debug("Menu tree updated with new commands.")

    def add(self, node_label):
        pass
