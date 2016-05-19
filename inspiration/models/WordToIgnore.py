from .InspirationBaseModelMixin import InspirationBaseModelMixIn
from django.db import models

class WordToIgnore(models.Model, InspirationBaseModelMixIn):
    word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return "<WordToIgnore - %s>" % (self.word)