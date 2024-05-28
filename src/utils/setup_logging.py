# utils/setup_logging.py

import logging
import os

def setup_logger(name, log_dir='log', log_file='app.log', log_level=logging.INFO):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_path = os.path.join(log_dir, log_file)

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Prevent adding duplicate handlers to logger
    if not logger.hasHandlers():
        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(log_level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger