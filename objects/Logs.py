import logging
logging.basicConfig(filename='debug.log', format='%(asctime)s %(message)s')

class Logs():

    def __init__(self) -> None:
        pass

    @staticmethod
    def msg(msg):
        print(msg)
        logging.debug(msg)
        return True

    @staticmethod
    def error(msg):
        print(msg)
        logging.error(msg)
        return True