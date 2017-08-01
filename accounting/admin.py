from django.contrib import admin
from .models import Post,AllImageOut,AllImageIn
# Register your models here.
admin.site.register(Post)
admin.site.register(AllImageOut)
admin.site.register(AllImageIn)
