from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000000)
    created_date = models.DateTimeField(default=datetime.now, blank=True)