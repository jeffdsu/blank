from django.db import models
from .InspirationBaseModelMixin import InspirationBaseModelMixIn


class InsightTag(models.Model, InspirationBaseModelMixIn):
    tag = models.ForeignKey('Tag')
    insight = models.ForeignKey('Insight', related_name='tags')