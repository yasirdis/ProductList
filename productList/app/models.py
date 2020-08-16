from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    Id = models.CharField(primary_key = True, max_length = 9)
    Name = models.CharField(max_length=20)
    Quantity = models.IntegerField()
    ImgSrc = models.CharField(max_length = 50)

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Phone=models.CharField(max_length=11)
    def __str__(self):
        return self.user.username
