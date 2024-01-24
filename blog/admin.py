from django.contrib import admin

# Register your models here.
from blog.models import Tag, Post

admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
  prepopulated_fileds = {"slug": ("title",)}
  list_diplay = ('slug', 'published_at')

admin.site.register(Post, PostAdmin)
