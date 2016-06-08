from enum import Enum
import json
import logging
import time


class blankLogMessage():

    def __init__(self, view):
        self.api=""
        self.msg = ""
        self.status = None
        self.user = None
        self.time = time.time()

    def add_log_msg(self, msg):
        self.msg += str(msg)

class blankLogging():

    logger = logging.getLogger('blank_logging')

    def __init__ (self, log_level = logging.WARN):
        self.logger.setLevel(log_level)

    @classmethod
    def write_log_message (cls, message, request, status):
        message.api = request.get_full_path()
        message.status = status
        message.user = request.user.id
        cls.logger.warning(json.dumps(message.__dict__))
        pass
