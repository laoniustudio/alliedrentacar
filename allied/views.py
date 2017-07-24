from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login

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