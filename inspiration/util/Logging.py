from enum import Enum
import json
import logging
import time


class blankLogMessage():

    def __init__(self, view):
        self.api=""
        self.log_msg = []
        self.status = None
        self.user = None
        self.time = time.time()
        self.query_params = None
        self.data = None

    def add_log_msg(self, log_msg):
        self.log_msg.append(str(log_msg))

class blankLogging():

    logger = logging.getLogger('blank_logging')

    def __init__ (self, log_level = logging.WARN):
        self.logger.setLevel(log_level)

    @classmethod
    def write_log_message (cls, message, request, response):
        message.api = request.get_full_path()
        message.status = response.status_code
        message.user = request.user.id
        message.query_params = request.query_params
        #message.data = response.data
        message.ip = cls.get_ip(request)
        cls.logger.warning(json.dumps(message.__dict__))


    @classmethod
    def get_ip(cls, request):
        http_x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if http_x_forwarded_for:
            ip_address = http_x_forwarded_for.split(',')[0]
        else:
            ip_address = request.META.get('REMOTE_ADDR')

        return ip_address
