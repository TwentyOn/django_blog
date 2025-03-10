from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from .models import Post
from .forms import EmailPostForm


# Create your views here.
def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 3)
    page_num = request.GET.get('page', 1)
    try:
        post_list = paginator.page(page_num)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    return render(request, 'blog/post/list.html', {'posts': post_list})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, publish__year=year, publish__month=month, publish__day=day, slug=post, status=Post.Status.PUBLISHED)

    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        cd = EmailPostForm(form)
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'form': form, 'post':post})