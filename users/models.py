from django.db import models
from django.contrib.auth.models import AbstractUser		#subclasses AbstractBaseUser
# Create your models here.

class CustomUser(AbstractUser):
	age = models.PositiveIntegerField(null = True, blank = True)

