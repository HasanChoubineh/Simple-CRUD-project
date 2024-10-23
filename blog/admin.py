from django.contrib import admin
from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'published', 'category']
    ordering = ['updated_at']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    ordering = ['created_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ['post', 'author', 'created_at', 'text']
    ordering = ['created_at']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = ['post', 'user', 'created_at']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = ['tag_name']