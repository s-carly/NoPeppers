from django.contrib import admin

# Register your models here.
from .models import Restaurant, Post, Comment

admin.site.register(Restaurant)
admin.site.register(Post)
admin.site.register(Comment)