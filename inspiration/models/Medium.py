from .InspirationBaseModelMixin import InspirationBaseModelMixIn
from django.db import models

class Medium(models.Model, InspirationBaseModelMixIn):
    type = models.CharField(max_length=255)
    icon_url = models.CharField(max_length=255)

    def __str__(self):
        return "<Author - %s %s>" % (self.first_name, self.last_name)