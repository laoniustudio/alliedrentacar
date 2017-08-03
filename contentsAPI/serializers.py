from rest_framework import serializers
from accounting.models import Post,DamgeOut,MoreImageIn


# all case
class PostSerializer(serializers.ModelSerializer):
    dateOutTime = serializers.DateTimeField(format="%m/%d/%Y")
    dateInTime = serializers.DateTimeField(format="%m/%d/%Y")
    class Meta:
        model = Post
        fields = '__all__'



# all Image in damage
class ImgInDamageSerializer(serializers.ModelSerializer):

    class Meta:
        model = DamgeOut
        fields = ['dashboardImg','frontImg','passFrontImg','passRearImg','rearImg','driveRearImg','driveFrontImg']

# all more image in damage
class ImgInMoreDamageSerializer(serializers.ModelSerializer):
    moreImgIn = serializers.SlugRelatedField(many=True, read_only=True, slug_field='damage')
    class Meta:
        model = Post
        fields = ['moreImgIn']