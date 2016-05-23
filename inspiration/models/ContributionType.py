from django.db import models
from django.contrib.auth.models import User
from .InspirationBaseModelMixin import InspirationBaseModelMixIn

class ContributionType(models.Model, InspirationBaseModelMixIn):
    name = models.CharField(max_length=255)