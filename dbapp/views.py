from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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

    author = request.user

    Post.objects.create(header=header, desc=desc, author=author)

    return redirect('/')

def api_info(request):
    return render(request, "api.html")


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        error = None
        
        if password != password_confirm:
            error = 'Пароли не совпадают'
        elif User.objects.filter(username=username).exists():
            error = 'Пользователь с таким именем уже существует'
        elif User.objects.filter(email=email).exists():
            error = 'Пользователь с такой почтой уже существует'
        
        if not error:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('/')
        
        return render(request, 'register.html', {'error': error})
    
    return render(request, 'register.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error = 'Неверное имя пользователя или пароль'
            return render(request, 'login.html', {'error': error})
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')