from django.db import models
from django.utils import timezone
# Create your models here.

class Day(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('title',max_length=200)
    text = models.TextField('text')
    date = models.DateTimeField('date',default=timezone.now)
