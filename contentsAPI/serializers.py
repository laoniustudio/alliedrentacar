from rest_framework import serializers
from accounting.models import Post,AllImageIn,AllImageOut,DamgeOut

class PostSerializer(serializers.ModelSerializer):
    dateOutTime = serializers.DateTimeField(format="%m/%d/%Y")
    dateInTime = serializers.DateTimeField(format="%m/%d/%Y")
    class Meta:
        model = Post
        fields = '__all__'

class ImgOutDamageSerializer(serializers.ModelSerializer):

    class Meta:
        model = DamgeOut
        fields = '__all__'