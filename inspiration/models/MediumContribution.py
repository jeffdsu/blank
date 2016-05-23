from django.db import models
from django.contrib.auth.models import User
from .InspirationBaseModelMixin import InspirationBaseModelMixIn
from .Contributor import Contributor
from .ContributionType import ContributionType
from .Medium import Medium

class MediumContribution(models.Model, InspirationBaseModelMixIn):
    contributor = models.ForeignKey(Contributor, null=True, on_delete=models.CASCADE)
    type = models.ForeignKey(ContributionType, null=True, on_delete=models.CASCADE)
    medium = models.ForeignKey(Medium, null=True, on_delete=models.CASCADE)
    rank = models.IntegerField()