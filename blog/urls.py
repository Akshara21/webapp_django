from django.urls import path
from . import views
from .views import (
    PostsListView,
    PostsDetailView,
    PostsCreateView,
    PostsUpdateView,
    PostsDeleteView,
    UserPostsListView
)

urlpatterns = [
    path('home/', views.PostsListView.as_view(), name = 'Blog-home'),
    path('user/<str:username>', views.UserPostsListView.as_view(), name = 'user-posts'),
    path('home/post/<int:pk>/', views.PostsDetailView.as_view(), name = 'post-detail'),
    path('post/new/', PostsCreateView.as_view(), name = 'post-create'),
    # since we are passing class as views we have to use as_view() along with the viewname
    path('about/', views.about, name = 'Blog-about'),
    path('latest/', views.latest, name = 'latest'),
    path('home/post/<int:pk>/update/', PostsUpdateView.as_view(), name='post-update'),
    path('home/post/<int:pk>/delete/', PostsDeleteView.as_view(), name='post-delete'),
]
