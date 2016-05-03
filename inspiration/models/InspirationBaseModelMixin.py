from rest_framework.response import Response


class InspirationBaseModelMixIn():

    @classmethod
    def get(cls, id):

        obj = cls.objects.get(id=id)

        if obj is None:
            raise Exception(Response(status=404, data="[404] %s[%s] not found"%(str(cls.__name__), id)))
        return obj

    def respond_ok(self, serializer, obj):
        return Response(serializer(obj).data, status=200)

    def respond_nothing_done(self):
        return Response("Nothing Done", status=200)

    def respond_not_found(self):
        return Response(status=404, data="%s with id of %d"%(type(self), self.id))


