from django.contrib import admin
from .models import Postings, Comment

# Register your models here.
class PostingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'user']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'user']


admin.site.register(Postings, PostingsAdmin)
admin.site.register(Comment, CommentAdmin)
