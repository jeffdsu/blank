from rest_framework.response import Response
from inspiration.util.Logging import blankLogging, blankLogMessage


class InspirationBaseViewMixIn():

    logger = blankLogging()

    def blank_logging_decorator(fn):

        def decorator(self, *args, **kwargs):
            self.log_msg = blankLogMessage(self)


            return fn(self, *args, **kwargs)

        return decorator

    # TODO - make this read in inputs
    def read_return_params(self):
        return {'top_10_keywords':1}

    @classmethod
    def respond(cls, log_message, request, response):

        cls.logger.write_log_message(log_message, request, response)

        return response

    @classmethod
    def respond_ok(cls, log_message, request, data):
        status=200
        response = Response(status=status, data=data)
        cls.logger.write_log_message(log_message, request, response)

        return response

    @classmethod
    def respond_updated(cls, log_message, request, data):
        status=200

        response = Response(status=status, data=data)
        cls.logger.write_log_message(log_message, request, response)

        return response

    @classmethod
    def respondToException(cls, exception, log_message, request):

        response = None
        if isinstance(exception.args[0], Response):
            response = exception.args[0]
        else:
            print(exception)
            response = Response(status=400, data="Unknown Issue")

        return cls.respond(log_message, request, response)

    @classmethod
    def respond_nothing_done(cls, log_message, request):
        msg="[200] Nothing Done"
        log_message.add_log_msg(msg)

        return cls.respond(log_message, request, Response(status=200, data=msg))





