from rest_framework import serializers
from accounting.models import Post,AllImage

class PostSerializer(serializers.ModelSerializer):
    dateOutTime = serializers.DateTimeField(format="%m/%d/%Y")
    dateInTime = serializers.DateTimeField(format="%m/%d/%Y")
    class Meta:
        model = Post
        fields = '__all__'