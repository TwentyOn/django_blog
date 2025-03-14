from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.conf import settings
from .models import Post
from .forms import EmailPostForm, CommentForm


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
    post = get_object_or_404(Post, publish__year=year, publish__month=month, publish__day=day, slug=post,
                             status=Post.Status.PUBLISHED)

    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} рекомендует вам почитать " \
                      f"{post.title}"
            message = f"Почитай {post.title} {post_url}\n\n" \
                      f"{cd['name']} ({cd['email']}) комментарий: {cd['comment']}"
            send_mail(subject, message, settings.EMAIL_HOST_USER,
                      [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'form': form, 'post': post, 'sent': sent})


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)

    form = CommentForm(data=request.POST)
    if form.is_valid():
        cd = form.save(commit=False)
        cd.post = post
        cd.save()
    return render(request, 'comment.html', {'form': form, 'post': post, 'comment': cd})