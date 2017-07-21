from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from accounting.models import Post
# Create your views here.

class PostAPIViewGet(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostAPIViewPost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer