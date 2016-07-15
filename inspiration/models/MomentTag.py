from django.db import models
from .InspirationBaseModelMixin import InspirationBaseModelMixIn


class MomentTag(models.Model, InspirationBaseModelMixIn):
    tag = models.ForeignKey('Tag')
    moment = models.ForeignKey('Moment', related_name='tags')