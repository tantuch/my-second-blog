from django.http import HttpResponse
from django.template import loader
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    template = loader.get_template('blog/post_list.html')
    context = {
        'posts': posts,
}
    return HttpResponse(template.render(context, request))
