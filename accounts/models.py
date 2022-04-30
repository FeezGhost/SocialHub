from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GenderChoices(models.TextChoices):
    MALE = 'Male', 'Male'
    FEMALE = 'Female', 'Female'
    OTHER = 'Other', 'Other'

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_pic = models.ImageField(default="default-profile.png")
    age = models.IntegerField(default=1)
    gender = models.CharField(choices=GenderChoices.choices, max_length=128,  default=GenderChoices.OTHER)
    def __str__(self):
        return str(self.user.username)
