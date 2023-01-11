from asyncio.log import logger
import logging
logging.basicConfig(filename='debug.log', format='%(asctime)s %(message)s')

class Logs():

    logger = None

    def __init__(self) -> None:
        if logger == None:
            self.logger = logging.getLogger()
        pass

    @staticmethod
    def msg(msg):
        print(msg)
        Logs.logger.debug(msg)
        return True

    @staticmethod
    def error(msg):
        print(msg)
        Logs.logger.error(msg)
        return True