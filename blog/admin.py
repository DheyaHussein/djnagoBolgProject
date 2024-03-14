from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Post, User)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
    # fields = ['__all__',]
    # list_display = ['title',]
# admin.site.register(Post)
# admin.site.register(User)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']




# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     fields = ['__all__',]