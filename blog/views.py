from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.conf import settings
from .models import Post
from .forms import EmailPostForm, CommentForm
from taggit.models import Tag
from django.db.models import Count

# Create your views here.
def post_list(request, tag_slug=None):
    posts = Post.published.all()
    tag = None
    if tag_slug:
        tag = Tag.objects.get(slug=tag_slug)
        #tag = get_object_or_404(Tag, slug=tag_slug)
        posts = Post.objects.filter(tags=tag)

    paginator = Paginator(posts, 3)
    page_num = request.GET.get('page', 1)
    try:
        post_list = paginator.page(page_num)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    return render(request, 'blog/post/list.html', {'posts': post_list, 'tag': tag})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, publish__year=year, publish__month=month, publish__day=day, slug=post,
                             status=Post.Status.PUBLISHED)

    comments = post.comments.filter(active=True)

    # Форма для комментирования пользователями
    form = CommentForm()

    post_tags = post.tags.values_list('id', flat=True) # метод извлекает список идентификаторов id для данного поста
    similar_posts = Post.published.filter(tags__in=post_tags).exclude(id=post.id) # запрос на получение всех постов с совпадающими тегами, кроме текущего
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4] # 4 поста с наибольшим количеством совпадающих тегов

    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'form': form,
                   'similar_posts': similar_posts})


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
    """Функция обработки POST запросов на добавление комментариев
       Декоратор requere_POST гарантирует, что функция не будет обрабатывать запросы отличиные от POST"""
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)

    form = CommentForm(data=request.POST)
    comment = None
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'blog/post/comment.html', {'form': form, 'post': post, 'comment': comment})
