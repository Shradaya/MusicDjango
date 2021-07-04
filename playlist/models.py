from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
class videoUpload(models.Model):
    Title = models.CharField(max_length=140)
    Thumbnail = models.ImageField(upload_to='videos/Thumbnail', blank=False)
    Price = models.IntegerField(default=100)
    Description = models.TextField(max_length=750)
    Video = models.FileField(upload_to='videos/', blank=False)

    def __str__(self):
        return self.Title

class Order(models.Model):
    orderID = models.AutoField(primary_key=True, null = False)
    userID = models.IntegerField(null=True)
    videoID = models.IntegerField(null=True)

    def __int__(self):
        return self.orderID
