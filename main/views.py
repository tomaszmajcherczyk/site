"""
Those are basically functions for my main/urls. They allow to perform some given tasks there, like adding a new post on
main/new
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import ImgPost
from .forms import ImgPostForm
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
# Create your views here.


def img_post_list(ListView):
    posts = ImgPost.objects.all()
    return render(ListView, 'lista.html', {'posts': posts})


@login_required()  # prevent from using this function when unlogged.
def new_post(request):
    form = ImgPostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(img_post_list)

    return render(request, 'new_post.html', {'form': form})


@login_required()
def edit_post(request, id):
    post = get_object_or_404(ImgPost, pk=id)
    form = ImgPostForm(request.POST or None, request.FILES or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect(img_post_list)

    return render(request, 'new_post.html', {'form': form})


@login_required()
def delete_post(request, id):
    post = get_object_or_404(ImgPost, pk=id)

    if request.method == 'POST':
        post.delete()
        return redirect(img_post_list)

    return render(request, 'confirm.html', {'post': post})
