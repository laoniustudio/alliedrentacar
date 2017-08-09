from django.shortcuts import render,get_object_or_404,redirect
from .models import Invitation
from .forms import InviteForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def invite(request):
  if request.method == 'POST':

      if User.objects.filter(email=request.POST['email']).exists():
          return render(request, 'invitations/invite.html',{'error':'The email has already registed!'})
      else:
            if request.POST["role"] == "user":
                is_staff = False
            else:
                is_staff = True
            invitation = Invitation(email=request.POST['email'],code=User.objects.make_random_password(20),staff=is_staff)


            invitation.save()
            invitation.send()

            return render(request, 'invitations/invite.html',{'msg':'Email has been invited'})

  else:
      return render(request, 'invitations/invite.html')

  return render(request,'invitations/invite.html')

def invite_accept(request, token):
  invitation = get_object_or_404(Invitation, code__exact=token)
  request.session['invitation'] = invitation.id
  return redirect('signup')