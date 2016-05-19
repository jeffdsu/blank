from django.db import models
from django.contrib.auth.models import User
from .InspirationBaseModelMixin import InspirationBaseModelMixIn

from inspiration.models import Medium

class Checkout(models.Model, InspirationBaseModelMixIn):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medium = models.ForeignKey('Medium', on_delete=models.CASCADE, )
    checkout_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return "<Checkout - %s - %s>" % (str(self.medium), str(self.user))