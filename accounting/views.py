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
    context_object_name = 'detail'

    def get_context_data(self, **kwargs):
        context = super(CaseListDetail, self).get_context_data(**kwargs)

        moreImgOut= Post.objects.get(pk=self.kwargs.get('pk')).moreImgOut.all()
        moreImgIn = Post.objects.get(pk=self.kwargs.get('pk')).moreImgIn.all()
        context['moreImgOut'] = moreImgOut
        context['moreImgIn'] = moreImgIn
        context['nihao'] = "<md-nav-item md-nav-click='goto('page8')' name='{% get_media_prefix%}{{ moreImgOut.showCount }},{% get_media_prefix%}{{ moreImgIn.showCount }}'>
                O{{ forloop.counter }}
            </md-nav-item>"

        # compare which has more image, and show number with more image
        if moreImgIn.__len__() > moreImgOut.__len__():
            showCounts = range(moreImgIn.__len__())
        else:
            showCounts = range(moreImgOut.__len__())



        return context



#logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

