# axe_builder/parser/parser.py

import asyncio
from functools import lru_cache
from pathlib import Path
from typing import List, Optional

from lark import Lark, UnexpectedInput, exceptions
from loguru import logger

from axe_builder.models.models import MenuCommand
from axe_builder.parser.transformer import AxeSyntaxTransformer


class AxeSyntaxParser:
    """
    A class to parse axe:Syntax strings into structured MenuCommand objects.
    """

    def __init__(self, grammar_file: Optional[str] = None):
        """
        Initializes the AxeSyntaxParser with the specified grammar.

        Args:
            grammar_file (Optional[str]): Path to the Lark grammar file. Defaults to 'axe_syntax.lark'.
        """
        self.grammar_file = grammar_file or "axe_syntax.lark"
        self.parser = self._initialize_parser()

    def _initialize_parser(self) -> Lark:
        """
        Initializes and returns the Lark parser with the specified grammar.

        Returns:
            Lark: Configured Lark parser instance.
        """
        grammar_path = Path(__file__).parent / self.grammar_file
        if not grammar_path.exists():
            logger.error(f"Grammar file not found at: {grammar_path}")
            raise FileNotFoundError(f"Grammar file not found at: {grammar_path}")

        with grammar_path.open(encoding='utf-8') as f:
            axe_syntax_grammar = f.read()

        parser = Lark(
            axe_syntax_grammar,
            start='start',
            parser='lalr',
            propagate_positions=True,
            maybe_placeholders=False
        )
        logger.debug("Lark parser initialized successfully.")
        return parser

    @lru_cache(maxsize=128)
    def parse(self, syntax_str: str) -> List[MenuCommand]:
        """
        Parses the given axe:Syntax string and returns a list of MenuCommand objects.

        Args:
            syntax_str (str): The axe:Syntax string to parse.

        Returns:
            List[MenuCommand]: Parsed MenuCommand objects.

        Raises:
            ValueError: If the syntax is invalid.
            RuntimeError: For unexpected parsing or transformation errors.
        """
        logger.info("Starting parsing of axe:Syntax.")
        try:
            parse_tree = self.parser.parse(syntax_str)
            transformer = AxeSyntaxTransformer()
            result = transformer.transform(parse_tree)
            if not isinstance(result, list):
                result = [result]
            self._validate_commands(result)
            logger.info("Parsing completed successfully.")
            return result
        except UnexpectedInput as e:
            logger.error(f"Syntax Error at line {e.line}, column {e.column}: {e}")
            raise ValueError(
                f"Invalid axe:Syntax input at line {e.line}, column {e.column}: {e}"
            ) from e
        except exceptions.VisitError as e:
            logger.error(f"Transformation Error: {e.orig}")
            raise RuntimeError(f"Error during transformation: {e.orig}") from e
        except Exception as e:
            logger.exception("Unexpected parsing error.")
            raise RuntimeError(f"An unexpected error occurred during parsing: {e}") from e

    def _validate_commands(self, commands: List[MenuCommand]) -> None:
        """
        Validates the list of MenuCommand objects to ensure data integrity.

        Args:
            commands (List[MenuCommand]): List of MenuCommand objects to validate.

        Raises:
            ValueError: If any command fails validation.
        """
        logger.debug("Validating parsed MenuCommand objects.")
        for cmd in commands:
            if not cmd.type or cmd.type not in {"M", "N"}:
                logger.error(f"Invalid MenuCommand type: {cmd.type}")
                raise ValueError(f"Invalid MenuCommand type: {cmd.type}")
            if cmd.operation and cmd.operation not in {"+", "="}:
                logger.error(f"Invalid operation '{cmd.operation}' in MenuCommand type '{cmd.type}'.")
                raise ValueError(f"Invalid operation '{cmd.operation}' in MenuCommand type '{cmd.type}'.")
            if cmd.count is not None and cmd.count <= 0:
                logger.error(f"MenuCommand count must be positive. Got: {cmd.count}")
                raise ValueError(f"MenuCommand count must be positive. Got: {cmd.count}")
            for sub in cmd.subcommands:
                if not sub.type or sub.type not in {"T", "."}:
                    logger.error(f"Invalid SubCommand type: {sub.type}")
                    raise ValueError(f"Invalid SubCommand type: {sub.type}")
                if sub.operation and sub.operation not in {"+", "="}:
                    logger.error(f"Invalid operation '{sub.operation}' in SubCommand type '{sub.type}'.")
                    raise ValueError(f"Invalid operation '{sub.operation}' in SubCommand type '{sub.type}'.")
                if sub.type == "T" and not sub.value:
                    logger.error("Title SubCommand must have a value.")
                    raise ValueError("Title SubCommand must have a value.")
                if sub.count is not None and sub.count <= 0:
                    logger.error(f"SubCommand count must be positive. Got: {sub.count}")
                    raise ValueError(f"SubCommand count must be positive. Got: {sub.count}")
        logger.debug("All MenuCommand objects validated successfully.")

    async def async_parse(self, syntax_str: str) -> List[MenuCommand]:
        """
        Asynchronously parses the given axe:Syntax string.

        Args:
            syntax_str (str): The axe:Syntax string to parse.

        Returns:
            List[MenuCommand]: Parsed MenuCommand objects.
        """
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self.parse, syntax_str)

    def reload_grammar(self) -> None:
        """
        Reloads the grammar file and reinitializes the parser.
        """
        logger.info("Reloading grammar and reinitializing parser.")
        self.parser = self._initialize_parser()
        self.parse.cache_clear()
        logger.debug("Grammar reloaded and parser reinitialized successfully.")

    # Singleton parser instance
_parser_instance = AxeSyntaxParser()

def parse_axesyntax(syntax_str: str) -> List[MenuCommand]:
    """
    Parses an axe:Syntax string and returns a list of MenuCommand objects.

    Args:
        syntax_str (str): The axe:Syntax string to parse.

    Returns:
        List[MenuCommand]: Parsed MenuCommand objects.

    Raises:
        ValueError: If the syntax is invalid.
        RuntimeError: For unexpected parsing or transformation errors.
    """
    return _parser_instance.parse(syntax_str)
