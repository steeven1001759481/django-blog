from django.shortcuts import render
from .models import Post

# Create your views here.
def indexView(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)
