from django.shortcuts import render
from .models import Post

# Create your views here.
def indexView(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def postView(request, id):
    postDetails = Post.objects.get(id=id)
    context = {
        'postDetails': postDetails,
    }
    return render(request, 'post.html', context)