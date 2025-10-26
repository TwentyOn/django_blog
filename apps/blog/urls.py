from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<slug:category_slug>/', views.PostListByCategory.as_view(), name='posts_by_category'),
    path('post/create/', views.CreatePost.as_view(), name='post_create'),
    path('post/<int:pk>/comments/create/', views.AddComment.as_view(), name='comment_create_view'),
    path('post/<slug:slug>/update/', views.UpdatePost.as_view(), name='post_update'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
