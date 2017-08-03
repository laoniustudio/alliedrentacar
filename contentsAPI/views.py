from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer,ImgOutDamageSerializer
from accounting.models import Post, DamgeOut
# Create your views here.

# get all the posts
class PostAPIViewGet(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostAPIViewPost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIGet(generics.RetrieveAPIView):
    serializer_class = ImgOutDamageSerializer
    queryset = DamgeOut.objects.all()
    lookup_field = 'post'