from clone.models import Image
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . forms import NewImageForm
from .email import send_welcome_email
from django.http import JsonResponse
# Create your views here.

def welcome(request):
    return render(request,'all-post/index.html')

@login_required(login_url='/accounts/login/')
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except Image.DoesNotExist:
        raise Http404()
    return render(request,"all-post/post.html", {"image":image})
    
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.poster = current_user
            image.save()
        return HttpResponseRedirect('welcome')
    else:
        form = NewImageForm()
    return render(request, 'new_post.html', {"form": form})    

# sending welcome email
    # send_welcome_email(name,email)