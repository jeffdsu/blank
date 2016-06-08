from rest_framework.response import Response
from inspiration.util import blankError


class InspirationBaseModelMixIn():

    @classmethod
    def get(cls, id):

        try:
            obj = cls.objects.get(id=id)

        except:
            kwargs = dict()
            kwargs['cls'] = cls
            kwargs['id'] = id
            cls.throw_not_found_exception(**kwargs)
        return obj

    @classmethod
    def search(cls, **kwargs):
        return cls.objects.filter(**kwargs)


    def respond_ok(self, obj, serializer):
        return Response(serializer(self).data, status=200)

    @classmethod
    def throw_not_found_exception(cls, **kwargs):
        raise Exception(Response(status=404, data=blankError(blankError.ERROR_TYPES.OBJ_NOT_FOUND, **kwargs).serialize()))

    def respond_not_found(self):
        return Response(status=404, data="[404] %s with id of %d"%(type(self), self.id))







