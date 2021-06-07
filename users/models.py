from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from hood.models import Mtaa
from phone_field import PhoneField
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mtaa = models.ForeignKey(Mtaa, on_delete=models.CASCADE, null=True, related_name='occupants')
    bio = models.TextField()
    cloudinary_image = CloudinaryField('image', null=True)
    # image = models.ImageField(default='default_fiis58.jpg',upload_to='hood_profile_pics')
    phone_number = PhoneField(blank=True, help_text='Contact phone number', E164_only=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} Profile"