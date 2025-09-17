from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm, CommentPostForm, SearchForm
from .models import Post, Comment
from taggit.models import Tag
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.http import require_POST
from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery


# Create your views here.
def post_list(request, tag_slug=None):
    if tag_slug:
        tag = Tag.objects.get(slug=tag_slug)
        post_list = Post.objects.filter(tags=tag)
    else:
        post_list = Post.published.all()
    paginator = Paginator(post_list, 2)
    page = request.GET.get('page', 1)
    try:
        posts_for_page = paginator.page(page)
    except EmptyPage:
        posts_for_page = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts_for_page = paginator.page(1)
    return render(request, 'blog/post/list.html', context={'posts': posts_for_page})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, publish__year=year, publish__month=month, publish__day=day, slug=post)
    tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=tags_ids).exclude(id=post.id) \
        .annotate(same_tags=Count('tags'))
    # print(similar_posts.query)
    similar_posts = similar_posts.order_by('-same_tags', '-publish')
    comments = Comment.objects.filter(post=post, active=True)
    comment_form = CommentPostForm()
    if request.user.is_authenticated:
        comment_form = CommentPostForm({'name': request.user.username})
    return render(request, 'blog/post/detail.html',
                  context={'post': post, 'form': comment_form, 'comments': comments, 'similar_posts': similar_posts})


def post_share(request, post_id):
    post = get_object_or_404(Post, pk=post_id, status=Post.Status.PUBLISHED)
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_mail(f'{data["name"]} рекомендует вам почитать {post.title}',
                      f'Ссылка: {request.build_absolute_uri(post.get_absolute_url())}\nКомментарий: {data["comment"]}',
                      settings.EMAIL_HOST_USER,
                      [data['email_to']],
                      )
            return HttpResponse(
                f'<h2>Сообщение отправлено успешно</h2><br><a href="{post.get_absolute_url()}">К списку постов</a>')
    else:
        form = EmailPostForm()
        return render(request, 'blog/post/share.html', context={'form': form, 'post': post})


@require_POST
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id, status=Post.Status.PUBLISHED)
    form = CommentPostForm(data=request.POST)
    comment = None
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'blog/post/includes/comment.html', context={'form': form, 'comment': comment, 'post': post})


def post_search(request):
    form = SearchForm()
    query = None
    result = []
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', 'body', config='russian')
            search_query = SearchQuery(query, config='russian')
            result = (Post.published.
                      annotate(search=search_vector, rang=SearchRank(search_vector, search_query)).
                      filter(search=query).order_by('-rang'))
    return render(request, 'blog/post/search.html', context={'form': form,
                                                             'query': query,
                                                             'results': result})
