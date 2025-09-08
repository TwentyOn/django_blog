from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<str:tag_slug>/', views.post_list, name='tag_post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/', views.post_share, name='share_post'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('search/', views.post_search, name='post_search')
]
