from django.contrib import admin
from .models import Post
from bookmark.models import Bookmark

# admin.site.register(Post)

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


admin.site.register(Bookmark, BookmarkAdmin)
