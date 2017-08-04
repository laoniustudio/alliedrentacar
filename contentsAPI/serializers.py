from rest_framework import serializers
from accounting.models import Post,DamgeOut,MoreImageIn


# all case
class PostSerializer(serializers.ModelSerializer):
    dateOutTime = serializers.DateTimeField(format="%m/%d/%Y")
    dateInTime = serializers.DateTimeField(format="%m/%d/%Y")
    class Meta:
        model = Post
        fields = '__all__'
# update post info
class PostSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['comment']

# all Image in damage
class ImgInDamageSerializer(serializers.ModelSerializer):

    class Meta:
        model = DamgeOut
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