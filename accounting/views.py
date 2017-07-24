from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from .models import Post
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

# Create your views here.

# homepage default view
class CaseList(ListView):
    model = Post
    template_name = 'accounting/dashboard.html'
    context_object_name = 'posts'



#logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

