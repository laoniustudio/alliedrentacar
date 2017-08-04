from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer,ImgInMoreDamageSerializer,ImgInDamageSerializer,ImgInMoreDamageUpdateSerializer,PostSerializerUpdate
from accounting.models import Post, DamgeOut,MoreImageIn
# Create your views here.
class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: # Ignore empty fields.
                filter[field] = self.kwargs[field]
        return get_object_or_404(queryset, **filter)  # Lookup the object

# get all the case
class PostAPIViewGet(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostAPIViewPost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#update case
class PostAPIViewUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerUpdate


# get and update all image in damage info
class DamageInDetailAPIGetUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = ImgInDamageSerializer
    queryset = DamgeOut.objects.all()
    lookup_field = 'post'

# get more image in damage info
class MoreDamageInDetailAPIGet(generics.ListAPIView):
    serializer_class = ImgInMoreDamageSerializer

    def get_queryset(self, **kwargs):
        post = self.kwargs['post']
        queryset = MoreImageIn.objects.filter(post__exact=post)
        return queryset

# update more image in damage info
class MoreDamageInDetailAPIUpdate(MultipleFieldLookupMixin,generics.RetrieveUpdateAPIView):
    serializer_class = ImgInMoreDamageUpdateSerializer
    queryset = MoreImageIn.objects.all()
    lookup_fields = ('post','id')


