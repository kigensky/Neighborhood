from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.db.models import Count
from cloudinary.models import CloudinaryField

# Create your models here.

class Mtaa(models.Model):
    title = models.CharField(max_length=100)
    cloudinary_image = CloudinaryField('image', null=True)
    # image = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.now)
    admin = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
        
class Post(models.Model):
    title = models.CharField(max_length=100)
    cloudinary_image = CloudinaryField('image', null=True)
    # image = models.ImageField(upload_to='images/')
    body = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    # location = models.ForeignKey(Mtaa, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title        
        
class Business(models.Model):
    title = models.CharField(max_length=100)
    cloudinary_image = CloudinaryField('image', null=True)
    email = models.CharField(max_length=100)
    body = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # location = models.ForeignKey(Mtaa, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "businesses"

    def __str__(self):
        return self.title        
        
class Essential(models.Model):
    title = models.CharField(max_length=100)
    cloudinary_image = CloudinaryField('image', null=True)
    officer = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    # location = models.ForeignKey(Mtaa, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
        