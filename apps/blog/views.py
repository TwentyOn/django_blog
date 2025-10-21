from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Главная страница'
        return context_data


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    slug_field = 'slug'  # имя поля модели, содержащего slug
