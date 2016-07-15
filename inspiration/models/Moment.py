from django.db import models
from django.contrib.auth.models import User
from .InspirationBaseModelMixin import InspirationBaseModelMixIn
from datetime import datetime

class Moment(models.Model, InspirationBaseModelMixIn):
    title = models.CharField(max_length=255)
    insight = models.ForeignKey('Insight', on_delete=models.CASCADE, null=True, related_name='moments')
    text = models.TextField(null=True)
    link = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey('MomentType', on_delete=models.CASCADE, null=True)
    submittion_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return "<Moment>"