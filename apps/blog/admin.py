from django.contrib import admin
from .models import Post, Category
from mptt.admin import DraggableMPTTAdmin

# Register your models here.
admin.site.register(Post)


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {'slug': ('title',)}
