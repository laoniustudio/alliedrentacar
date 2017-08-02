from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.conf import settings
from reportlab.pdfgen import canvas
from django.http import HttpResponse
# Create your views here.

# homepage default view
class CaseList(ListView):
    model = Post
    template_name = 'accounting/dashboard.html'
    context_object_name = 'posts'
# case detail view
class CaseListDetail(DetailView):
    model = Post
    template_name = 'accounting/caseDetail.html'
    context_object_name = 'detail'

    def get_context_data(self, **kwargs):
        context = super(CaseListDetail, self).get_context_data(**kwargs)

        moreImgOut= Post.objects.get(pk=self.kwargs.get('pk')).moreImgOut.all()
        moreImgIn = Post.objects.get(pk=self.kwargs.get('pk')).moreImgIn.all()
        allImgOut = Post.objects.get(pk=self.kwargs.get('pk')).allImgOut
        allImgIn = Post.objects.get(pk=self.kwargs.get('pk')).allImgIn
        mediaUrl = settings.MEDIA_URL
        staticUrl = settings.STATIC_URL

        # ----------------------All Image show--------------------------------------#
        context['dashboardImgOut'] = mediaUrl + str(allImgOut.dashboardImg)
        context['frontImgOut'] = mediaUrl + str(allImgOut.frontImg)
        context['passFrontImgOut'] = mediaUrl + str(allImgOut.passFrontImg)
        context['passRearImgOut'] = mediaUrl + str(allImgOut.passRearImg)
        context['rearImgOut'] = mediaUrl + str(allImgOut.rearImg)
        context['driveRearOut'] = mediaUrl + str(allImgOut.driveRear)
        context['driveFrontOut'] = mediaUrl + str(allImgOut.driveFront)
        context['dashboardImgIn'] = mediaUrl + str(allImgIn.dashboardImg)
        context['frontImgIn'] = mediaUrl + str(allImgIn.frontImg)
        context['passFrontImgIn'] = mediaUrl + str(allImgIn.passFrontImg)
        context['passRearImgIn'] = mediaUrl + str(allImgIn.passRearImg)
        context['rearImgIn'] = mediaUrl + str(allImgIn.rearImg)
        context['driveRearIn'] = mediaUrl + str(allImgIn.driveRear)
        context['driveFrontIn'] = mediaUrl + str(allImgIn.driveFront)



        #----------------------More Image show--------------------------------------#
        # compare which has more image, and show number with more image
        if moreImgIn.__len__() > moreImgOut.__len__():
            counts = moreImgIn.__len__()
        else:
            counts = moreImgOut.__len__()
        content = ""
        for index in range(counts):
            page = "goto('page"+str(index+1+7)+"')"

            # as the number of imageOut and imageIn may not equal, so the loop may out of range
            try:
                imageOutURL = mediaUrl + str(moreImgOut[index].moreImage)
            except:
                imageOutURL = staticUrl + "/images/notfound.png"
            try:
                imageInURL = mediaUrl + str(moreImgIn[index].moreImage)
            except:
                imageInURL = staticUrl + "/images/notfound.png"
            html = "<md-nav-item md-nav-click=" + page + " name="+imageOutURL+ ","+imageInURL+">O"+str(index+1)+"</md-nav-item>"
            content = content+html
        context['content'] = content

        return context



def toPDF(request,pk):
    moreImgOut = Post.objects.get(pk=pk).moreImgOut.all()
    moreImgIn = Post.objects.get(pk=pk).moreImgIn.all()
    allImgOut = Post.objects.get(pk=pk).allImgOut
    allImgIn = Post.objects.get(pk=pk).allImgIn
    post = Post.objects.get(pk=pk)

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="'+ post.contractNumber +'.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.

    image = settings.BASE_DIR+settings.STATIC_URL+"images/logo.png"
    p.drawImage(image, 150, 700, width=300, height=137, mask=None)
    p.drawString(100, 600, "Contract No. : "+post.contractNumber)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


# logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

