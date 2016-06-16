from django.db import models
from django.contrib.auth.models import User
from .InspirationBaseModelMixin import InspirationBaseModelMixIn
from .Contributor import Contributor
from .ContributionType import ContributionType
from .Medium import Medium

class MediumLink(models.Model, InspirationBaseModelMixIn):
    medium = models.ForeignKey('Medium', on_delete=models.CASCADE, null=True, related_name='links')
    link = models.TextField(null=True)