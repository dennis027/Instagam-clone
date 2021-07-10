from django.http  import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def welcome(request):
    return render(request,'all-post/index.html')

@login_required(login_url='/accounts/login/')
def image(request):
    return render(request,'registration/login.html')