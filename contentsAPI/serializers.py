from rest_framework import serializers
from accounting.models import Post,DamageIn,MoreImageIn,Car
from invitation.models import Invitation
from django.contrib.auth.models import User


# all case
class PostSerializer(serializers.ModelSerializer):
    dateOutTime = serializers.DateTimeField(format="%m/%d/%Y")
    dateInTime = serializers.DateTimeField(format="%m/%d/%Y")
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Post
        fields = ['username','contractNumber','plateNumber','dateOutTime','dateInTime','status','damage']
# update post comment
class PostSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['status','comment']

# all Image in damage
class ImgInDamageSerializer(serializers.ModelSerializer):

    class Meta:
        model = DamageIn
        fields = ['dashboardImg','frontImg','passFrontImg','passRearImg','rearImg','driveRearImg']



# get all more image in damage
class ImgInMoreDamageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoreImageIn
        fields = ['id','damage']

# update more image in damage
class ImgInMoreDamageUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoreImageIn
        fields = ['damage']

# users : get
class UsersGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name','is_staff','username','email','date_joined']

# users : get Permission
class PermissionGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','is_staff']


# get invitation
class InvitationGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invitation
        fields = '__all__'

# get cars
class CarGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['id','unitNumber','plateNumber','model','status']

# get cars detail
class CarDetailGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'