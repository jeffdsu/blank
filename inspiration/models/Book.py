from django.db import models
from django.contrib.auth.models import User
from .InspirationBaseModelMixin import InspirationBaseModelMixIn

class Book(models.Model, InspirationBaseModelMixIn):
    author = models.ForeignKey('Author', null=True, on_delete=models.SET_NULL, related_name='books_authors')
    title = models.CharField(max_length=255)
    pub_date = models.DateField(null=True)
    summary = models.TextField()
    cover_url = models.CharField(max_length=255)

    def __str__(self):
        return "<Book - %s - %s>" % (self.title, str(self.author))


