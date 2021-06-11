from django.shortcuts import render,redirect

# Create your views here.


def HomeView(request):
    return render(request,'core/home.html')