# axe_builder/utils/utils.py

from pathlib import Path
from typing import Optional

from axe_builder.logger.logger import logger


def read_file(file_path: str) -> str:
    """
    Reads the content of a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: Content of the file.
    """
    try:
        path = Path(file_path)
        content = path.read_text(encoding="utf-8")
        logger.debug(f"Read content from {file_path}")
        return content
    except Exception as e:
        logger.error(f"Failed to read file {file_path}: {e}")
        raise


def write_file(file_path: str, content: str) -> None:
    """
    Writes content to a file.

    Args:
        file_path (str): Path to the file.
        content (str): Content to write.
    """
    try:
        path = Path(file_path)
        path.write_text(content, encoding="utf-8")
        logger.debug(f"Wrote content to {file_path}")
    except Exception as e:
        logger.error(f"Failed to write file {file_path}: {e}")
        raise


def validate_syntax(syntax: str) -> bool:
    """
    Validates the axe:Syntax string format.

    Args:
        syntax (str): The axe:Syntax string to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    # Placeholder for actual validation logic
    return True
