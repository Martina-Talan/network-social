from django.contrib import admin
from .models import User, NewPost, Following, Like

# Register your models here.
admin.site.register(User)
admin.site.register(NewPost)
admin.site.register(Following)
admin.site.register(Like)
