from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

# Create your views here.

# homepage default view
class CaseList(ListView):
    model = Post
    template_name = 'accounting/dashboard.html'
    context_object_name = 'posts'

class CaseListDetail(DetailView):
    model = Post
    template_name = 'accounting/caseDetail.html'
    context_object_name = 'details'

#logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

