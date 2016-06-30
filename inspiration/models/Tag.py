from django.db import models
from .InspirationBaseModelMixin import InspirationBaseModelMixIn


class Tag(models.Model, InspirationBaseModelMixIn):
    name = models.CharField(max_length=255)