# tests/logger/test_logger.py

from axe_builder.logger.logger import logger


def test_logger_configuration():
    try:
        logger.info("Test logger info message")
        logger.debug("Test logger debug message")
        logger.error("Test logger error message")
        assert True
    except Exception:
        assert False
