from rest_framework.response import Response
from inspiration.util.Logging import blankLogging, blankLogMessage


class InspirationBaseViewMixIn():

    logger = blankLogging()

    def blank_logging_decorator(fn):

        def decorator(self, *args, **kwargs):
            from inspiration.util.Logging import blankLogMessage
            self.log_msg = blankLogMessage(self)
            return fn(self, *args, **kwargs)

        return decorator

    # TODO - make this read in inputs
    def read_return_params(self):
        return {'top_10_keywords':1}

    def respondToException(self, exception):

        self.logger.write_log_message(self.log_msg)

        if isinstance(exception.args[0], Response):
            return exception.args[0]
        else:
            print(exception)
            return Response(status=400, data="Unknown Issue")

    def respond_nothing_done(self):
        msg = "[200] Nothing Done"
        status = 200
        self.log_msg.add_log_msg(msg)
        self.logger.write_log_message(self.log_msg, self.request, status)
        return Response(msg, status=status)
