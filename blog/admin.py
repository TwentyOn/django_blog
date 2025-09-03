from django.contrib import admin
from .models import Post, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish', 'status']
    list_filter = ['status', 'publish']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    autocomplete_fields = ['author']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'create']
    list_filter = ['active', 'create', 'update']
    search_fields = ['name', 'post']
