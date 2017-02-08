from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts_all = Post.objects.all()
    context = {'posts_all':posts_all}
    return render(request, 'blog/post_list.html', context)
