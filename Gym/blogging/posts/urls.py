from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='home'),
    # path('posts/<int:pk>/', views.posts, name='post-detail'),
    path('posts/<int:pk>/update/', views.post_update, name='post-update'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post-delete'),
    # path('posts/create/', views.post_create, name='post-create'),
    # path('blogs/', views.blogs, name='blogs'),
    # path('search/', views.search, name='search'),
    #  class based search view
    path('', views.IndexView.as_view(), name='home'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('posts/create/', views.PostCreateView.as_view(), name='post-create'),
    path('search/', views.SearchView.as_view(), name='search'),
]
