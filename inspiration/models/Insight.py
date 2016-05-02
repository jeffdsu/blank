from django.db import models
from django.contrib.auth.models import User
from inspiration.models import Book, Checkout
from .InspirationBaseModelMixin import InspirationBaseModelMixIn
from django.db.models import Q

class Insight(models.Model, InspirationBaseModelMixIn):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.TextField()
    checkout = models.ForeignKey(Checkout, null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    valid = models.BooleanField(default=False)

    def __str__(self):
        return "<Insight - %s>" % (str(self.lesson))

    @classmethod
    def search(cls, book, valid=True, **kwargs):
        return Insight.objects.filter(book=book, valid=valid, **kwargs)