from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Post):
    Title =  models.CharField(max_length=200)
    Text= models.CharField(default=0)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, default= User.get(id=1))
    Pub_date = models.DateTimeField
    Create_date = models.DateTimeField

