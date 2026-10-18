import logging

logger = logging.getLogger("module_1")
logger.setLevel(logging.DEBUG)

def process_data(data: list):
    logger.debug("Processing the data...")
    logger.info("Processing completed.")