from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Hood(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.now)
    admin = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
        
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title        