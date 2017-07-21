from django.db import models

# Create your models here.

class Post (models.Model):

    contractNumber = models.CharField(max_length=200, blank= True)
    plateNumber = models.CharField(max_length=200,blank= True)
    dateOutTime = models.DateTimeField()
    dateInTime = models.DateTimeField()
    STATUS_CHOICES = (
        ('ALL', 'All'),
        ('ONRENT', 'On Rent'),
        ('REVIEW', 'Ready for review'),
        ('PASS', 'Pass'),
        ('FAIL', 'Fail'),
    )
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='REVIEW')
    rentOut = models.BooleanField(default=False)
    damage =  models.BooleanField(default=False)
    def __str__(self):
        if self.contractNumber:
            return self.contractNumber
        else:
            return self.plateNumber

class AllImage(models.Model):
    post = models.ForeignKey(Post,related_name='moreImg')
    dashboardImg = models.ImageField(upload_to="images")
    frontImg = models.ImageField(upload_to="images")
    passFrontImg = models.ImageField(upload_to="images")
    passRearImg = models.ImageField(upload_to="images")
    rearImg = models.ImageField(upload_to="images")
    driveRear = models.ImageField(upload_to="images")
    driveFront = models.ImageField(upload_to="images")
    moreImage = models.ImageField(upload_to="images")