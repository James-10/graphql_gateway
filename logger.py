import logging

from config import Config

def configure_logger(logger_name:str):
    "Configure the logger to send logs to the console"

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

def get_logger(logger_name:str = Config.appname):
    return configure_logger(logger_name)


