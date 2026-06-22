from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('post', views.post_page),
    path('postdb/', views.postdb),
    path('api-info', views.api_info)
]