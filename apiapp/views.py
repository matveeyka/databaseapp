from django.shortcuts import render
from django.http import JsonResponse
from dbapp.models import Post
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def api_posts_list(request):
    posts = Post.objects.all()
    
    data = [{"header": post.header, "desc": post.desc} for post in posts]
    
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

def info(request):
    return JsonResponse([{"info": "Отправьте GET запрос на list/ или POST запрос на post/ для работы с API. Полная информация на 127.0.0.1:8000/api-info"}], safe=False, json_dumps_params={'ensure_ascii': False})

@csrf_exempt
def api_post(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            api_header = data.get('header')
            api_desc = data.get('desc')
            
            if not api_header:
                return JsonResponse({"error": "Поле 'header' обязательно для заполнения"}, status=400)
            
            Post.objects.create(header=api_header, desc=api_desc)
            return JsonResponse({"status": "success"}, status=201)
            
        except json.JSONDecodeError:
            return JsonResponse({"error": "Неверный формат JSON"}, status=400)
            
    return JsonResponse({"error": "Метод не поддерживается"}, status=405)