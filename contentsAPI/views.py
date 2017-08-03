from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer,ImgInMoreDamageSerializer,ImgInDamageSerializer
from accounting.models import Post, DamgeOut,MoreImageIn
# Create your views here.

# get all the case
class PostAPIViewGet(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostAPIViewPost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# get all image in damage info
class DamageInDetailAPIGet(generics.RetrieveAPIView):
    serializer_class = ImgInDamageSerializer
    queryset = DamgeOut.objects.all()
    lookup_field = 'post'
# update all image in damage info
class DamageInDetailAPIUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = ImgInDamageSerializer
    queryset = DamgeOut.objects.all()
    lookup_field = 'post'

# get more image in damage info
class MoreDamageInDetailAPIGet(generics.RetrieveAPIView):
    serializer_class = ImgInMoreDamageSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'