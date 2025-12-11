from axe_syntax.axe_builder.logger import logger


def test_logger_configuration():
    try:
        logger.info("Test logger info message")
        logger.debug("Test logger debug message")
        logger.error("Test logger error message")
        assert True
    except Exception:
        assert False
