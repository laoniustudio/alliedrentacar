from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post
from django.utils import timezone
# Create your views here.


class CaseList(ListView):
    model = Post
    template_name = 'accounting/dashboard.html'
    context_object_name = 'posts'


