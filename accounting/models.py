from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import os
# Create your models here.

class Post (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contractNumber = models.CharField(max_length=200, blank= True)
    plateNumber = models.CharField(max_length=200,blank= True)
    dateOutTime = models.DateTimeField()
    dateInTime = models.DateTimeField(blank=True,null=True)
    STATUS_CHOICES = (
        ('On Rent', 'On Rent'),
        ('Ready for review', 'Ready for review'),
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
    )
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Ready for review')
    damage = models.BooleanField(default=False)
    comment = models.TextField(blank=True)

    def __str__(self):
        if self.contractNumber:
            return self.contractNumber
        else:
            return self.plateNumber


class AllImageOut(models.Model):
    post = models.OneToOneField(Post,related_name="allImgOut")
    mainImg = models.ImageField(upload_to="images")
    dashboardImg = models.ImageField(upload_to="images")
    frontImg = models.ImageField(upload_to="images")
    passFrontImg = models.ImageField(upload_to="images")
    passRearImg = models.ImageField(upload_to="images")
    rearImg = models.ImageField(upload_to="images")
    driveRear = models.ImageField(upload_to="images")
    driveFront = models.ImageField(upload_to="images")

    def __str__(self):
        return self.post.contractNumber



class MoreImageOut(models.Model):
    post = models.ForeignKey(Post,related_name='moreImgOut')
    moreImage = models.ImageField(upload_to="images")
    def __str__(self):
        return self.post.contractNumber



class AllImageIn(models.Model):
    post = models.OneToOneField(Post,related_name='allImgIn')
    mainImg = models.ImageField(upload_to="images")
    dashboardImg = models.ImageField(upload_to="images")
    frontImg = models.ImageField(upload_to="images")
    passFrontImg = models.ImageField(upload_to="images")
    passRearImg = models.ImageField(upload_to="images")
    rearImg = models.ImageField(upload_to="images")
    driveRear = models.ImageField(upload_to="images")
    driveFront = models.ImageField(upload_to="images")

    def __str__(self):
        return self.post.contractNumber


class MoreImageIn(models.Model):
    post = models.ForeignKey(Post,related_name='moreImgIn')
    moreImage = models.ImageField(upload_to="images")
    damage = models.BooleanField(default=False)


    def __str__(self):
        return "ContractNo : "+self.post.contractNumber+",ID : "+str(self.id)

class DamageIn(models.Model):
    post = models.OneToOneField(Post,related_name='damgeOut')
    dashboardImg = models.BooleanField(default=False)
    frontImg = models.BooleanField(default=False)
    passFrontImg = models.BooleanField(default=False)
    passRearImg = models.BooleanField(default=False)
    rearImg = models.BooleanField(default=False)
    driveRearImg = models.BooleanField(default=False)
    driveFrontImg = models.BooleanField(default=False)

    def __str__(self):
        return self.post.contractNumber

class Car(models.Model):
    unitNumber = models.CharField(max_length=200,unique=True)
    plateNumber = models.CharField(max_length=200,unique=True)
    model = models.CharField(max_length=500)
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to="cars")

    def __str__(self):
        return self.unitNumber

    def imagename(self):
        return os.path.basename(self.image.name)
