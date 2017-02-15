from django.http import HttpResponse
from django.template import loader
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    template = loader.get_template('blog/post_list.html')
    context = {
        'posts': posts,
}
    return HttpResponse(template.render(context, request))

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})
