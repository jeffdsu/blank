from .InspirationBaseModelMixin import InspirationBaseModelMixIn
from django.db import models

class MediumType(models.Model, InspirationBaseModelMixIn):
    name = models.CharField(max_length=255)
    icon_url = models.CharField(max_length=255)

    def __str__(self):
        return "<MediumType - %s>" % (self.name)