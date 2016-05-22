from rest_framework.response import Response


class InspirationBaseViewMixIn():

    @classmethod
    def respondToException(self, exception):
        if isinstance(exception.args[0], Response):
            return exception.args[0]
        else:
            print(exception)
            return Response(status=400, data="Unknown Issue")

    @classmethod
    def respond_not_found(self, err_msg):
        return Response(status=404, data=err_msg)
