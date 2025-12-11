# axe_builder/logger/logger.py

import sys

from loguru import logger

# Remove default logger
logger.remove()

# Console sink with colored output and INFO level
logger.add(
    sys.stderr,
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>",
    enqueue=True,
)

# File sink with rotation and DEBUG level
logger.add(
    "axe_builder.log",
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}",
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    enqueue=True,
    serialize=False,
)

# JSON sink for structured logging
logger.add(
    "axe_builder.json",
    level="DEBUG",
    format='{"time": "{time:YYYY-MM-DD HH:mm:ss}", "level": "{level}", "message": "{message}"}',
    rotation="50 MB",
    retention="30 days",
    compression="gzip",
    enqueue=True,
    serialize=True,
)
