from django.shortcuts import render,redirect,Http404
from invitation.models import Invitation
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
def homesignin(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request=request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('accounting:caselist')

        else:
            return render(request,'signin.html',{'error':'Username or password is not correct !'})
    return render(request, 'signin.html')

def signup(request):

    if 'invitation' in request.session:
        # Retrieve the invitation object.
        invitation = Invitation.objects.get(id=request.session['invitation'])
        if request.method == "POST":

            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            username = request.POST['username']
            password = request.POST['password']
            email = invitation.email

            auth_user = authenticate(request=request, username=username, password=password)

            if auth_user is None:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
                user.save()
                login(request, auth_user)
                invitation = Invitation.objects.filter(email=email)
                invitation.delete()

                return redirect('accounting:caselist')

            else:
                return render(request, 'signup.html', {'error': 'Username already exists'})
        return render(request, 'signup.html')
    else:
        return Http404

