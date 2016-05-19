from django.db import models
from django.contrib.auth.models import User
from inspiration.models import Medium, Checkout
from .InspirationBaseModelMixin import InspirationBaseModelMixIn
from django.db.models import Q

class Insight(models.Model, InspirationBaseModelMixIn):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.TextField()
    checkout = models.ForeignKey(Checkout, null=True, on_delete=models.CASCADE)
    medium = models.ForeignKey('Medium', on_delete=models.CASCADE)
    valid = models.BooleanField(default=False)

    def __str__(self):
        return "<Insight - %s>" % (str(self.lesson))

    @classmethod
    def search(cls, **kwargs):
        print(kwargs)
        return Insight.objects.filter(**kwargs)