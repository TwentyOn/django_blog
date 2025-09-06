from django import template
from ..models import Post
from django.db.models import Count

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/lates_posts.html')
def latest_posts(count=5):
    lates_posts = Post.published.all().order_by('-publish')
    return {'latest_posts': lates_posts[:count]}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).exclude(total_comments=0).order_by('-total_comments')[:count]
