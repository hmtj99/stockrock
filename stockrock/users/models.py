from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        default='default.jpg', upload_to='profile_pics')
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        self.user.username
