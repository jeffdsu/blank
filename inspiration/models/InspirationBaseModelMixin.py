from rest_framework.response import Response


class InspirationBaseModelMixIn():

    @classmethod
    def get(cls, id):

        objs = cls.objects.filter(id=id)

        if len(objs) != 1:
            raise Exception(Response(status=404, data="[404] %s[%s] not found"%(str(cls.__name__), id)))
        return objs[0]

    def respond_ok(self, serializer, obj):
        return Response(serializer(obj).data, status=200)

    def respond_not_found(self):
        return Response(status=404, data="%s with id of %d"%(type(self), self.id))

