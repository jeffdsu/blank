from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .InspirationBaseModelMixin import InspirationBaseModelMixIn

class User(AbstractBaseUser, InspirationBaseModelMixIn):
    username = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = 'id'

    class Meta:
        db_table = 'auth_user'
    pass
