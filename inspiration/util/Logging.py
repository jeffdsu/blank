from enum import Enum
import json
import logging
import time


class blankLogMessage():

    def __init__(self, view):
        self.api=""
        self.log_msg = ""
        self.status = None
        self.user = None
        self.time = time.time()
        self.query_params = None

    def add_log_msg(self, log_msg):
        self.log_msg += str(log_msg)

class blankLogging():

    logger = logging.getLogger('blank_logging')

    def __init__ (self, log_level = logging.WARN):
        self.logger.setLevel(log_level)

    @classmethod
    def write_log_message (cls, message, request, status):
        message.api = request.get_full_path()
        message.status = status
        message.user = request.user.id
        message.query_params = request.query_params
        cls.logger.warning(json.dumps(message.__dict__))
