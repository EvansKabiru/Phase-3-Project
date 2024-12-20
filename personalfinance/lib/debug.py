import logging

# Setup logger for debugging purposes
def setup_debug_logger():
    logger = logging.getLogger("debug")
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    return logger
