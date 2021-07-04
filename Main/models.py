from django.db import models
from datetime import datetime
# Create your models here.

from django.db import models
class message(models.Model):
    FullName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100, blank=False)
    Phone = models.CharField(max_length=10)
    Message = models.TextField(max_length=500, blank=False)
    Date = models.DateTimeField(datetime.now())

    def __str__(self):
        return self.FullName
