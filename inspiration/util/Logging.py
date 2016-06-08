from enum import Enum
import json
import logging


class blankLogMessage():

    def __init__(self, view):
        self.api=""
        self.msg = ""
        self.status = None

    def add_log_msg(self, msg):
        self.msg += str(msg)

class blankLogging():

    logger = logging.getLogger('blank_logging')

    def __init__ (self, log_level = logging.WARN):
        self.logger.setLevel(log_level)

    def write_log_message (self, message, request, status):
        message.api = request.get_full_path()
        message.status = status
        print(json.dumps(message.__dict__))
        pass
