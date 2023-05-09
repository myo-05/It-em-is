from django.contrib import admin
from .models import Postings, Comment

# Register your models here.
admin.site.register(Postings)
admin.site.register(Comment)