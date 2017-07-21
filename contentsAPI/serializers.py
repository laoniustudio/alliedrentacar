from rest_framework import serializers
from accounting.models import Post,AllImage

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'