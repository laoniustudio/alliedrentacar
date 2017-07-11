from django.shortcuts import render

def homesignin(request):
    return render(request, 'signin.html')