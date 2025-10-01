from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile_user_model(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='profile')
    image = models.ImageField(upload_to="profile_user/", null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    website = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"username : {self.user}   /   email :  {self.email}"
    
    