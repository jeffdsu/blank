from django.db import models
from django.contrib.auth.models import User
from .InspirationBaseModelMixin import InspirationBaseModelMixIn

class Medium(models.Model, InspirationBaseModelMixIn):
    type = models.ForeignKey('MediumType')
    title = models.CharField(max_length=255)
    pub_date = models.DateField(null=True)
    summary = models.TextField(null=True)
    cover = models.CharField(max_length=255, null=True)
    valid = models.BooleanField(default=False)

    def __str__(self):
        return "<Medium [%s]- %s - %s>" % (self.title, self.type, str(self.contributions))

    @classmethod
    def search(cls, **kwargs):
        return Medium.objects.filter(**kwargs)





