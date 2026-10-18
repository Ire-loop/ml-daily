import logging

logger = logging.getLogger("module2")
logger.setLevel(logging.INFO)

def save_data(data: list):
    if not isinstance(data, list):
        logger.error("The data type is not list.")
    if len(data) == 0:
        logger.warning("The data is empty.")        