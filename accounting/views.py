from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.conf import settings
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.utils import formats
from .utility import CaseDetailExtend
from django.views.generic.base import TemplateView
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

        #initial utility
        utility = CaseDetailExtend(self.kwargs.get('pk'))
        utility.getImage()

        # ----------------------All Image show--------------------------------------#
        context['dashboardImgOut'] = utility.mediaUrl + str(utility.allImgOut.dashboardImg)
        context['frontImgOut'] = utility.mediaUrl + str(utility.allImgOut.frontImg)
        context['passFrontImgOut'] = utility.mediaUrl + str(utility.allImgOut.passFrontImg)
        context['passRearImgOut'] = utility.mediaUrl + str(utility.allImgOut.passRearImg)
        context['rearImgOut'] = utility.mediaUrl + str(utility.allImgOut.rearImg)
        context['driveRearOut'] = utility.mediaUrl + str(utility.allImgOut.driveRear)
        context['driveFrontOut'] = utility.mediaUrl + str(utility.allImgOut.driveFront)
        context['dashboardImgIn'] = utility.mediaUrl + str(utility.allImgIn.dashboardImg)
        context['frontImgIn'] = utility.mediaUrl + str(utility.allImgIn.frontImg)
        context['passFrontImgIn'] = utility.mediaUrl + str(utility.allImgIn.passFrontImg)
        context['passRearImgIn'] = utility.mediaUrl + str(utility.allImgIn.passRearImg)
        context['rearImgIn'] = utility.mediaUrl + str(utility.allImgIn.rearImg)
        context['driveRearIn'] = utility.mediaUrl + str(utility.allImgIn.driveRear)
        context['driveFrontIn'] = utility.mediaUrl + str(utility.allImgIn.driveFront)



        #----------------------More Image show--------------------------------------#
        # compare which has more image, and show number with more image

        content = ""
        for index in range(utility.counts):
            page = "goto('"+str(index)+"')"

            # as the number of imageOut and imageIn may not equal, so the loop may out of range
            try:
                imageOutURL = utility.mediaUrl + str(utility.moreImgOut[index].moreImage)
            except:
                imageOutURL = utility.staticUrl + "images/notfound.png"
            try:
                imageInURL = utility.mediaUrl + str(utility.moreImgIn[index].moreImage)
            except:
                imageInURL = utility.staticUrl + "images/notfound.png"

            bindData = "O"+str(index+1)
            idName = "n"+str(index+7)
            html = "<md-nav-item md-nav-click=" + page + " id="+idName+" name="+imageOutURL+ ","+imageInURL+">"+bindData+"<span class='badge badge-pill badge-warning' ng-show="+bindData+" >!</span></md-nav-item>"
            content = content+html
        context['content'] = content

        # ----------------------damage for image show--------------------------------------#


        return context



def toPDF(request,pk):
    # initial utility
    utility = CaseDetailExtend(pk)
    utility.getImage()

    post = Post.objects.get(pk=pk)

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="'+ post.contractNumber +'.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.

    logo = settings.BASE_DIR + utility.staticUrl + "images/logo.png"

    # print all the pages for Rent out
    imageOutCount = 7 + utility.moreImgOut.__len__()
    for index in range(imageOutCount):
        if index == 0:
            image = settings.BASE_DIR + utility.mediaUrl + str(utility.allImgOut.dashboardImg)
        elif index == 1:
            image = settings.BASE_DIR + utility.mediaUrl + str(utility.allImgOut.frontImg)
        elif index == 2:
            image = settings.BASE_DIR + utility.mediaUrl + str(utility.allImgOut.passFrontImg)
        elif index == 3:
            image = settings.BASE_DIR + utility.mediaUrl + str(utility.allImgOut.passRearImg)
        elif index == 4:
            image = settings.BASE_DIR + utility.mediaUrl + str(utility.allImgOut.rearImg)
        elif index == 5:
            image = settings.BASE_DIR + utility.mediaUrl + str(utility.allImgOut.driveRear)
        elif index == 6:
            image = settings.BASE_DIR + utility.mediaUrl + str(utility.allImgOut.driveFront)
        else:#more image
            image = settings.BASE_DIR + utility.mediaUrl + str(utility.moreImgOut[index-7].moreImage)

        # set position name
        if index<=6:
            positionNameOut = utility.nameDic[index]
        else:
            positionNameOut = "Other"+str(index-6)

        #start print on PDF
        p.drawImage(logo, 200, 730, width=200, height=91, mask=None)
        p.drawString(100, 700, "Contract No. : "+post.contractNumber)
        p.drawString(300, 700, "Date In : " + str(formats.date_format(post.dateInTime,"SHORT_DATETIME_FORMAT")))
        p.drawString(100, 650, "Unit No. : " + post.plateNumber)
        p.drawString(300, 650, "Date Out. : " + str(formats.date_format(post.dateOutTime,"SHORT_DATETIME_FORMAT")))
        p.drawString(200, 580, "Photo Position: "+positionNameOut+"       Before")
        p.drawImage(image, 50, 180, width=500, height=375, mask=None)
        p.drawString(100, 150, "Damage:")
        p.showPage()

    # print all the pages for check in
    imageInCount = 7 + utility.moreImgIn.__len__()
    for index in range(imageInCount):
        if index == 0:
            image = settings.BASE_DIR + utility.mediaUrl + str(utility.allImgIn.dashboardImg)
        elif index == 1:
            image = settings.BASE_DIR + utility.mediaUrl + str(utility.allImgIn.frontImg)
        elif index == 2:
            image = settings.BASE_DIR + utility.mediaUrl + str(utility.allImgIn.passFrontImg)
        elif index == 3:
            image = settings.BASE_DIR + utility.mediaUrl + str(utility.allImgIn.passRearImg)
        elif index == 4:
            image = settings.BASE_DIR + utility.mediaUrl + str(utility.allImgIn.rearImg)
        elif index == 5:
            image = settings.BASE_DIR + utility.mediaUrl + str(utility.allImgIn.driveRear)
        elif index == 6:
            image = settings.BASE_DIR + utility.mediaUrl + str(utility.allImgIn.driveFront)
        else:  # more image
            image = settings.BASE_DIR + utility.mediaUrl + str(utility.moreImgIn[index - 7].moreImage)

        # set position name
        if index <= 6:
            positionNameIn = utility.nameDic[index]
        else:
            positionNameIn = "Other" + str(index - 6)

        # start print on PDF
        p.drawImage(logo, 200, 730, width=200, height=91, mask=None)
        p.drawString(100, 700, "Contract No. : " + post.contractNumber)
        p.drawString(300, 700, "Date In : " + str(formats.date_format(post.dateInTime, "SHORT_DATETIME_FORMAT")))
        p.drawString(100, 650, "Unit No. : " + post.plateNumber)
        p.drawString(300, 650, "Date Out. : " + str(formats.date_format(post.dateOutTime, "SHORT_DATETIME_FORMAT")))
        p.drawString(200, 580, "Photo Position: " + positionNameIn + "       After")
        p.drawImage(image, 50, 180, width=500, height=375, mask=None)
        p.drawString(100, 150, "Damage:")
        p.showPage()


    # Close the PDF object cleanly, and we're done.
    p.save()
    return response


# logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

# show toast template
class ToastShow(TemplateView):
    template_name = 'accounting/toast-template.html'