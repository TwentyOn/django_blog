from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('post/create/', views.CreatePost.as_view(), name='post_create'),
    path('post/<slug:slug>/update', views.UpdatePost.as_view(), name='post_update'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
