from django.db import models
from django.contrib.auth.models import User
from .InspirationBaseModelMixin import InspirationBaseModelMixIn

class Medium(models.Model, InspirationBaseModelMixIn):
    contributors = models.ForeignKey('MediumContribution', null=True, on_delete=models.SET_NULL, related_name='works')
    type = models.ForeignKey('MediumType', null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    pub_date = models.DateField(null=True)
    summary = models.TextField(null=True)
    cover = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "<Medium [%s]- %s - %s>" % (self.title, self.type, str(self.contributors))

    @classmethod
    def search(cls, **kwargs):
        return Medium.objects.filter(**kwargs)

