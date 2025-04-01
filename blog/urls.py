import os.path

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('tag/<slug:tag_slug>/',
         views.post_list, name='post_list_by_tag'),
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',  # дружественный для индексации url
         views.post_detail,
         name='post_detail'),
    path('<int:post_id>/share', views.post_share, name='post_share'),
    path('<int:post_id>/comment', views.post_comment, name='post_comment'),
]
