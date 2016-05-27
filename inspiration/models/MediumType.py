from .InspirationBaseModelMixin import InspirationBaseModelMixIn
from django.db import models

class MediumType(models.Model, InspirationBaseModelMixIn):
    # TODO need to migrate to plural
    name = models.CharField(max_length=255)
    # TODO - Jeff this should not be true.
    singular_eng_noun = models.CharField(null=True,max_length=255)
    icon_url = models.CharField(max_length=255)

    def __str__(self):
        return "<MediumType - %s>" % (self.name)