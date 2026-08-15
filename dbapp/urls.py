from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('post', views.post_page),
    path('postdb/', views.postdb),
    path('api-info', views.api_info),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]