from .InspirationBaseModelMixin import InspirationBaseModelMixIn
from django.db import models

class WordsToIgnore(models.Model, InspirationBaseModelMixIn):
    word = models.CharField(max_length=50)

    def __str__(self):
        return "<WordsToIgnore - %s>" % (self.word)