"""
Those are basically functions for my main/urls. They allow to perform some given tasks there, like adding a new post on
main/new
"""
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import ImgPost
from .forms import ImgPostForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('all_posts')  # after si
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def img_post_list(request):
    posts = ImgPost.objects.all()
    # all this code responsigle for pagination is also pasted in the one_tag function, how to avoid code duplication
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)  # shows 10 contacts per page

    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


#  those 3 lines are what for? commented them and no change?
    # tag = request.GET.get('tag')
    # if tag:
    #     posts = posts.filter(img_tags__tag_name=tag)

    return render(request, 'lista.html', {'posts': posts})


@login_required()  # prevent from using this function when unlogged.
def new_post(request):
    user = request.user
    form = ImgPostForm(request.POST or None, request.FILES or None, initial={'author': user})
    if form.is_valid():
        form.save()
        return redirect(img_post_list)

    return render(request, 'new_post.html', {'form': form})


@login_required()
def edit_post(request, id):
    post = get_object_or_404(ImgPost, pk=id)
    if request.user != post.author:
        raise PermissionError
    form = ImgPostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect(img_post_list)

    return render(request, 'new_post.html', {'form': form})


@login_required()
def delete_post(request, id):
    post = get_object_or_404(ImgPost, pk=id)
    if request.user != post.author:
        raise PermissionError
    if request.method == 'POST':
        post.delete()
        return redirect(img_post_list)

    return render(request, 'confirm.html', {'post': post})


def one_tag(request, name):
    posts = ImgPost.objects.filter(img_tags__tag_name=name)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)  # shows 10 contacts per page

    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'lista.html', {'posts': posts})
