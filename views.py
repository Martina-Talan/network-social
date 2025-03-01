from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import PostForm
from django.http import JsonResponse
from .models import User, NewPost, Following, Like
import json



def index(request):
    posts = NewPost.objects.order_by("-timestamp")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, "network/index.html", {
        "form": PostForm(),
        "posts": posts,
        "page": page,
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")



def new_post(request):
# Create a new post
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.posted_by = request.user  
            new_post.save()
            return redirect('index') 
    else:
        form = PostForm()
    return render(request, 'network/index.html', {
        'form': form
    })

@login_required
def user_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    posts = NewPost.objects.filter(posted_by=user).order_by('-timestamp')
    current_user = request.user
    is_following = Following.objects.filter(user=current_user, followed=user).exists()
    followers_count = Following.objects.filter(followed=user).count()
    following_count = Following.objects.filter(user=user).count()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    

    return render(request, "network/user_profile.html", {
        "user": user,
        "form": PostForm(),
        "posts": posts,
        "followers_count": followers_count,
        "following_count": following_count,
        "page": page, 
        "is_following": is_following,
    })


@login_required
def follow_user(request, user_id):
    user_to_follow = User.objects.get(pk=user_id)
    
    # Check if the user is not already following
    if not Following.objects.filter(user=request.user, followed=user_to_follow).exists():
        Following.objects.create(user=request.user, followed=user_to_follow)
    
    return redirect('user_profile', user_id=user_id)

@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = User.objects.get(pk=user_id)
    
    # Check if the user is already following
    if Following.objects.filter(user=request.user, followed=user_to_unfollow).exists():
        Following.objects.filter(user=request.user, followed=user_to_unfollow).delete()
    
    return redirect('user_profile', user_id=user_id)
    

def following_posts(request):
    current_user = request.user
    following_users = Following.objects.filter(user=current_user).values_list('followed', flat=True)
    posts = NewPost.objects.filter(posted_by__in=following_users).order_by('-timestamp')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    return render(request, 'network/following.html',{
         'page': page,  

    })

@login_required
def edit_post(request, post_id):
    post = NewPost.objects.get(pk=post_id)
    if request.method == 'POST':
        data = json.loads(request.body)
        post_content = request.POST.get('post_content')
        post.post = data["post_content"]
        post.save()
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False, 'message': 'Invalid request'})


@login_required   
def like_post(request, post_id):
    post = NewPost.objects.get(pk=post_id)
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
        liked = False
    else:
        post.likes.add(user)
        liked = True

    return JsonResponse({'success': True, 'liked': liked, 'likes': post.likes.count()})
    JsonResponse({'success': True, 'likes': post.likes.count()})


@login_required
def unlike_post(request, post_id):
    if request.method == 'POST':
        post = NewPost.objects.get(pk=post_id)
        user = request.user

        # Check if the user has already liked the post
        if user in post.likes.all():
            post.likes.remove(user)
            return JsonResponse({'success': True, 'likes': post.likes.count()})
        else:
            return JsonResponse({'success': False, 'message': 'You have not liked this post.'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})


