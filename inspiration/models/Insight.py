from django.db import models
from django.contrib.auth.models import User
from inspiration.models import Medium, Checkout
from .InspirationBaseModelMixin import InspirationBaseModelMixIn
from django.db.models import Q
from random import randint

class Insight(models.Model, InspirationBaseModelMixIn):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.TextField()
    checkout = models.ForeignKey(Checkout, null=True, on_delete=models.CASCADE)
    medium = models.ForeignKey('Medium', on_delete=models.CASCADE)
    valid = models.BooleanField(default=False)
    personal = models.BooleanField()

    def __str__(self):
        return "<Insight - %s>" % (str(self.lesson))

    @classmethod
    def random_for_medium(cls, medium, keywords=None, **kwargs):

        query = Q(medium=medium, valid=True, personal=False)
        keyword_q = Q()

        for keyword in keywords:
            keyword_q |= Q(lesson__icontains=keyword.word)

        insight_count = cls.objects.filter(query & keyword_q).count()

        if insight_count == 0:
            cls.throw_not_found_exception()

        random_idx = randint(0, insight_count - 1)
        random_cls = cls.objects.filter(query & keyword_q)[random_idx]


        return random_cls