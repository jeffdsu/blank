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
            raise Exception(Response(status=404, data=blankError(blankError.ERROR_TYPES.OBJ_NOT_FOUND, **kwargs).serialize()))
        return obj

    @classmethod
    def search(cls, **kwargs):
        return cls.objects.filter(**kwargs)

    @classmethod
    def respond_already_found(cls, **kwargs):
        return Response("[422] %s already found with [%s]"%(cls.__name__, kwargs), status=422)

    def respond_ok(self, obj, serializer):
        return Response(serializer(self).data, status=200)

    def respond_not_found(self):
        return Response(status=404, data="[404] %s with id of %d"%(type(self), self.id))







