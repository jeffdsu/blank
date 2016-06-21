from django.db import models
from django.contrib.auth.models import User
from .InspirationBaseModelMixin import InspirationBaseModelMixIn
from .Contributor import Contributor
from .ContributionType import ContributionType
from .Medium import Medium

class MediumContribution(models.Model, InspirationBaseModelMixIn):
    medium = models.ForeignKey('Medium', on_delete=models.CASCADE, null=True, related_name='contributions')
    contributor = models.ForeignKey(Contributor, null=True, on_delete=models.CASCADE)
    type = models.ForeignKey(ContributionType, null=True, on_delete=models.CASCADE)
    rank = models.IntegerField(null=True)