import numpy as np
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("This is an info message")
logging.debug("this is a debug message")
logging.warning("this is a warning message")
logging.error("this is an error message")
logging.critical("this is a critical message")