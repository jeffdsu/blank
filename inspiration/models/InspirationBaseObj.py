from django.db import models

class InspirationBaseObj():
    pass

    @classmethod
    def get(cls, id):
        return cls.objects.filter(id=id)[0]
