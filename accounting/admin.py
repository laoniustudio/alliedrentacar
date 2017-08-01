from django.contrib import admin
from .models import Post,AllImageOut,AllImageIn,MoreImageIn,MoreImageOut
# Register your models here.
admin.site.register(Post)
admin.site.register(AllImageOut)
admin.site.register(AllImageIn)
admin.site.register(MoreImageIn)
admin.site.register(MoreImageOut)
