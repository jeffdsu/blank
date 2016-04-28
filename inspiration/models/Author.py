from django.db import models
from .InspirationBaseObj import InspirationBaseObj
from .InspirationBaseModelMixin import InspirationBaseModelMixIn

class Author(models.Model, InspirationBaseModelMixIn):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_initial = models.CharField(max_length=1, null=True)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return "<Author - %s %s>" % (self.first_name, self.last_name)