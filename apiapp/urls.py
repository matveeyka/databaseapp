from django.urls import path, include
from . import views

urlpatterns = [
    path('list', views.api_posts_list),
    path('', views.info),
    path('post', views.api_post)
]