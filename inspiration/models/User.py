from .InspirationBaseModelMixin import InspirationBaseModelMixIn
from django.contrib.auth.models import User as BaseUser

class User(BaseUser, InspirationBaseModelMixIn):

    def __str__(self):
        return "<User - %s %s>" % (self.first_name, self.last_name)