from django.shortcuts import render,redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "main.html", {"posts": posts})

def post_page(request):
    return render(request, 'post.html')

def postdb(request):
    header = request.POST.get('header')
    desc = request.POST.get('desc')

    Post.objects.create(header=header, desc=desc)

    return redirect('/')

def api_info(request):
    return render(request, "api.html")