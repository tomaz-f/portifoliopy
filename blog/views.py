from django.shortcuts import render
from blog.models import Post, Comment

def blog_index(request):
    post = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)