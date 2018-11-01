from django.shortcuts import render, redirect

from .models import Post

def post(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('post')

    posts = Post.objects.all()
    return render(
        request,
        'post/post_list.html',
        {'posts' : posts}
    )
