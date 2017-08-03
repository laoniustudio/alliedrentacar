from .models import Post
from django.conf import settings

class CaseDetailExtend():

    def __init__(self,pk):
        self.pk = pk

    def getImage(self):
        self.moreImgOut = Post.objects.get(pk=self.pk).moreImgOut.all()
        self.moreImgIn = Post.objects.get(pk=self.pk).moreImgIn.all()
        self.allImgOut = Post.objects.get(pk=self.pk).allImgOut
        self.allImgIn = Post.objects.get(pk=self.pk).allImgIn
        self.mediaUrl = settings.MEDIA_URL
        self.staticUrl = settings.STATIC_URL
        self.nameDic = ['Dashboard','Front','Pass-Front','Pass-Rear','Rear','Drive-Rear','Drive-Front']

        if self.moreImgIn.__len__() > self.moreImgOut.__len__():
            self.counts = self.moreImgIn.__len__()
        else:
            self.counts = self.moreImgOut.__len__()





