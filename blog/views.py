from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 3)
    page_num = request.GET.get('page', 1)
    post_list = paginator.page(page_num)
    return render(request, 'blog/post/list.html', {'posts': post_list})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, publish__year=year, publish__month=month, publish__day=day, slug=post, status=Post.Status.PUBLISHED)

    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )
