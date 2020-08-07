from django.contrib import admin
from .models import Post, Author, Category, Comment, PostView
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', ]

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','comment_count', 'featured']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','title']

admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(PostView)