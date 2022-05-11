import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    logger.setLevel(logging.CRITICAL)

    logger.debug("This is debug Statement")
    logger.info("This is info Statement")
    logger.warning("This is warning Statement")
    logger.error("This is error Statement")
    logger.critical("This is critical Statement")
