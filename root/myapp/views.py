import datetime
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment

def post_list(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'index.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    # post = get_object_or_404(Post, id=post_id)
    comments = post.comment_set.all()
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'post.html', context)