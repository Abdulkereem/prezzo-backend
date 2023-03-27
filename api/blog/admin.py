from django.contrib import admin
from .models import Blog
from .forms import BlogPostForm

class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostForm

    

admin.site.register(Blog, BlogPostAdmin)
