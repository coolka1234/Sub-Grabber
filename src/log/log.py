import logging
from math import log
import os

forrmater=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def setup_loger(name, log_file, level=logging.DEBUG):
    handler=logging.FileHandler(log_file)
    handler.mode="w"
    handler.setFormatter(forrmater)
    logger=logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

log_instance=setup_loger("log", "log.log")
