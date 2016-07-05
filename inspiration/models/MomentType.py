from django.db import models
from django.contrib.auth.models import User
from .InspirationBaseModelMixin import InspirationBaseModelMixIn

class MomentType(models.Model, InspirationBaseModelMixIn):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "<Moment Type %s>" % self.name