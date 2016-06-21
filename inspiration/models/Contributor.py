from django.db import models
from django.contrib.auth.models import User
from .InspirationBaseModelMixin import InspirationBaseModelMixIn
from .ContributionType import ContributionType

class Contributor(models.Model, InspirationBaseModelMixIn):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_initial = models.CharField(max_length=1, null=True)
    date_of_birth = models.DateField(null=True)
    biography = models.TextField(null=True)

    def __str__(self):
        return "<Contributor - %s %s>" % (self.first_name, self.last_name)

    @classmethod
    def search(cls, **kwargs):
        return Contributor.objects.filter(**kwargs)