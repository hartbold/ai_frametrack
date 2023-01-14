from asyncio.log import logger
import logging

class Logs():

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_logger():
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler("debug.log"),
                logging.StreamHandler()
            ]
        )

        return logging.getLogger(__name__)

    @staticmethod
    def msg(msg):
        print(msg)
        logger = Logs.get_logger()
        logger.debug(msg)
        return True

    @staticmethod
    def error(msg):
        print(msg)
        logger = Logs.get_logger()
        logger.error(msg)
        return True