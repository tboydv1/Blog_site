from django.contrib import admin
from .models import Post
# Register your models here.

#Register DB models to use int the admin dashboard
admin.site.register(Post)
