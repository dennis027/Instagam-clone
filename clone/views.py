from .models import *
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . forms import *
from .email import send_welcome_email
from django.http import JsonResponse

# Create your views here.

def welcome(request):
    posts =Image.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.poster = current_user
            image.save()
            send_welcome_email(name,email)
        return HttpResponseRedirect('welcome')
    else:
        form = NewImageForm()
    return render(request, 'all-post/index.html', {"form": form,"posts":posts} ) 
    # return render(request,'all-post/index.html')

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

# def search_results(request):

#     if 'post' in request.GET and request.GET["image"]:
#         search_term = request.GET.get("image")
#         searched_images = Image.search_by_name(search_term)
#         message = f"{search_term}"

#         return render(request, 'all-news/search.html',{"message":message,"images": searched_images})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'all-news/search.html',{"message":message})    



@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = DetailsForm(request.POST, request.FILES)
        if form.is_valid():
                Profile.objects.filter(id=current_user.profile.id).update(bio=form.cleaned_data["bio"])
                profile = Profile.objects.filter(id=current_user.profile.id).first()
                profile.profile_pic.delete()
                profile.profile_pic=form.cleaned_data["profile_pic"]
                profile.save()
        return redirect('profile')

    else:
        form = DetailsForm()
    
    return render(request, 'edit_profile.html',{"form": form})        


@login_required(login_url='/accounts/login/')
def other_profile(request,id):
    profile_user=User.objects.filter(id=id).first()
    posts=Image.objects.all()
    following=Follower.objects.filter(username=profile_user.username).all()
    followingcount=len(following)
    followers=Follower.objects.filter(followed=profile_user.username).all()
    followercount=len(followers)
    return render(request, 'others.html',{"profile_user": profile_user,"posts":posts,"followingcount":followingcount,"followercount":followercount})

@login_required(login_url='/accounts/login/')
def search(request):
    posts=Image.objects.all()
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        following=Follower.objects.filter(username=search_term).all()
        followingcount=len(following)
        followers=Follower.objects.filter(followed=search_term).all()
        followercount=len(followers)
        searched_user = User.objects.filter(username=search_term).first()
        if searched_user:
            message = f"{search_term}"
            return render(request, 'others.html',{"profile_user": searched_user,"posts":posts,"followingcount":followingcount,"followercount":followercount})
        else:
            message = "The username you are searching for does not exist.Thank you for visiting InstaNight."
            return render(request,{"message":message})

@login_required(login_url='/accounts/login/')
def profile(request):
    posts=Image.objects.all()
    current_user = request.user
    following=Follower.objects.filter(username=current_user.username).all()
    followingcount=len(following)
    followers=Follower.objects.filter(followed=request.user.username).all()
    followercount=len(followers)
    if request.method == 'POST':
        form = DetailsForm(request.POST, request.FILES)
        form1 = PostForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        if form1.is_valid():
            post = form1.save(commit=False)
            post.profile = current_user.profile
            post.save()

        return redirect('profile')

    else:
        form = DetailsForm()
        form1 = PostForm()
    
    return render(request, 'profile.html', {"form":form,"form1":form1,"posts":posts,"followingcount":followingcount,"followercount":followercount})            

def post_detail(request, slug):
    template_name = 'comment.html'
    post = get_object_or_404(Image, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})    