import logging
import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

logger = logging.getLogger()

formatter = logging.Formatter()
logger.setLevel(LOG_LEVEL)

handler = logging.StreamHandler()
handler.setFormatter(formatter)
if logger.hasHandlers():
    logger.handlers.clear()

logger.addHandler(handler)
