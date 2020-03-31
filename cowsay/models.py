from django.db import models
from django.conf import settings
from django.utils import timezone

class Cowsay(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField('date created', default=timezone.now)