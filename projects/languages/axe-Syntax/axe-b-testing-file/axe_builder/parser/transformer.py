# axe_builder/parser/transformer.py

from typing import List, Optional

from axe_builder.models.models import MenuCommand, SubCommand
from lark import Transformer, v_args
from loguru import logger


class TransformationError(Exception):
    """Custom exception for transformation errors."""

    pass


@v_args(inline=True)
class AxeSyntaxTransformer(Transformer):
    """
    Transforms the parse tree from axe:Syntax into MenuCommand and SubCommand objects.
    """

    def start(self, *commands) -> List[MenuCommand]:
        """
        Transforms the start rule into a list of MenuCommand objects.
        """
        logger.debug(f"Transforming start with commands: {commands}")
        return list(commands)

    def command_line(self, *commands) -> List[MenuCommand]:
        """
        Transforms the command_line rule into a list of MenuCommand objects.
        """
        logger.debug(f"Transforming command_line with commands: {commands}")
        return list(commands)

    def command(self, command) -> MenuCommand:
        """
        Transforms the command rule into a single MenuCommand object.
        """
        logger.debug(f"Transforming command: {command}")
        if not isinstance(command, MenuCommand):
            logger.error("Transformed command is not a MenuCommand instance.")
            raise TransformationError("Invalid command transformation.")
        return command

    def menu_command(self, menu_type: str, *operations) -> MenuCommand:
        """
        Transforms the menu_command rule into a MenuCommand object.
        """
        logger.debug(
            f"Transforming menu_command: type={menu_type}, operations={operations}"
        )
        operation = None
        count = None
        subcommands: List[SubCommand] = []

        idx = 0
        while idx < len(operations):
            op, operand = operations[idx], operations[idx + 1]
            logger.debug(f"Processing operation: {op} with operand: {operand}")
            if op == "+":
                if isinstance(operand, int):
                    if count is not None:
                        logger.error(
                            "Multiple counts specified for a single menu_command."
                        )
                        raise TransformationError("Multiple counts specified.")
                    count = operand
                elif isinstance(operand, SubCommand):
                    subcommands.append(operand)
                else:
                    logger.error(
                        f"Invalid operand type for '+' operator: {type(operand)}"
                    )
                    raise TransformationError(
                        f"Invalid operand type for '+' operator: {type(operand)}"
                    )
            elif op == "=":
                if isinstance(operand, int):
                    if count is not None:
                        logger.error(
                            "Multiple counts specified for a single menu_command."
                        )
                        raise TransformationError("Multiple counts specified.")
                    count = operand
                elif isinstance(operand, SubCommand):
                    subcommands.append(operand)
                else:
                    logger.error(
                        f"Invalid operand type for '=' operator: {type(operand)}"
                    )
                    raise TransformationError(
                        f"Invalid operand type for '=' operator: {type(operand)}"
                    )
            else:
                logger.error(f"Unsupported operator: {op}")
                raise TransformationError(f"Unsupported operator: {op}")
            idx += 2

        if count is None and any(sub.type == "T" for sub in subcommands):
            logger.error(
                "MenuCommand with title subcommand must have a count.")
            raise TransformationError(
                "MenuCommand with title subcommand must have a count."
            )

        menu_command = MenuCommand(
            type=menu_type, operation=operation, count=count, subcommands=subcommands
        )
        logger.debug(f"Created MenuCommand: {menu_command}")
        return menu_command

    def sub_command(self, sub_type: str, *operations) -> SubCommand:
        """
        Transforms the sub_command rule into a SubCommand object.
        """
        logger.debug(
            f"Transforming sub_command: type={sub_type}, operations={operations}"
        )
        operation = None
        value = None
        count = None

        idx = 0
        while idx < len(operations):
            op, operand = operations[idx], operations[idx + 1]
            logger.debug(f"Processing operation: {op} with operand: {operand}")
            if op == "=":
                if sub_type == "T":
                    if not isinstance(operand, str):
                        logger.error(
                            "Title SubCommand must have a string value.")
                        raise TransformationError(
                            "Title SubCommand must have a string value."
                        )
                    value = operand
                elif sub_type == ".":
                    if not isinstance(operand, int):
                        logger.error(
                            "Custom SubCommand must have an integer count.")
                        raise TransformationError(
                            "Custom SubCommand must have an integer count."
                        )
                    count = operand
                operation = op
            elif op == "+":
                operation = op
                # Future extensions for '+' operator can be handled here
            else:
                logger.error(f"Unsupported operator in sub_command: {op}")
                raise TransformationError(
                    f"Unsupported operator in sub_command: {op}")
            idx += 2

        if sub_type == "T" and not value:
            logger.error("Title SubCommand must have a value.")
            raise TransformationError("Title SubCommand must have a value.")

        if sub_type == "." and count is None:
            logger.error("Custom SubCommand must have a count.")
            raise TransformationError("Custom SubCommand must have a count.")

        sub_command = SubCommand(
            type=sub_type, operation=operation, value=value, count=count
        )
        logger.debug(f"Created SubCommand: {sub_command}")
        return sub_command

    def operator(self, op: str) -> str:
        """
        Transforms the operator rule into a string.
        """
        logger.debug(f"Operator parsed: {op}")
        return op

    def operand(self, operand) -> Optional[object]:
        """
        Transforms the operand rule into an object (int or str).
        """
        logger.debug(f"Operand parsed: {operand}")
        return operand

    def MENU_TYPE(self, token) -> str:
        """
        Transforms the MENU_TYPE token into a string.
        """
        menu_type = token.value
        logger.debug(f"MENU_TYPE parsed: {menu_type}")
        return menu_type

    def SUB_TYPE(self, token) -> str:
        """
        Transforms the SUB_TYPE token into a string.
        """
        sub_type = token.value
        logger.debug(f"SUB_TYPE parsed: {sub_type}")
        return sub_type

    def NUM_VAR(self, token) -> int:
        """
        Transforms the NUM_VAR token into an integer.
        """
        num_var = int(token.value.strip("{}"))
        logger.debug(f"NUM_VAR parsed: {num_var}")
        return num_var

    def value(self, token) -> str:
        """
        Transforms the value token into a string.
        """
        val = token.value.strip('"')
        logger.debug(f"value parsed: {val}")
        return val

    def __default__(self, data, children, meta):
        """
        Handles any unprocessed rules.
        """
        logger.warning(
            f"Unhandled rule: {data} with children: {children} at line {meta.line}, column {meta.column}"
        )
        return children
