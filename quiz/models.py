from django.db import models

class Quiz(models.Model):
    ques = models.TextField(default='')
    ans = models.BooleanField()
