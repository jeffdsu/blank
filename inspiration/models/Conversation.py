from django.db import models
from django.contrib.auth.models import User
from .InspirationBaseModelMixin import InspirationBaseModelMixIn

class Conversation(models.Model, InspirationBaseModelMixIn):
    insight = models.ForeignKey('Insight', on_delete=models.CASCADE, null=True, related_name='conversations')
    text = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "<Conversation>"