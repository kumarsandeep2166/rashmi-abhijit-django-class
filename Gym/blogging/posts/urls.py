from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/<int:pk>/', views.posts, name='post-detail'),
    path('blogs/', views.blogs, name='blogs'),
    path('search/', views.search, name='search'),
]
