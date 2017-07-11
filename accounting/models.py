from django.db import models

# Create your models here.

class Post (models.Model):
    dashboardImg = models.ImageField()
    frontImg = models.ImageField()
    passFrontImg = models.ImageField()
    passRearImg = models.ImageField()
    rearImg = models.ImageField()
    driveRear = models.ImageField()
    driveFront = models.ImageField()

class MoreImage(models.Model):
    post = models.ForeignKey(Post,related_name='moreImg')
    image = models.ImageField()