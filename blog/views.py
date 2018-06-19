from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User

def post_list(request):
    posts = Post.objects.all()
#    me = User.objects.get(username='admin')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})