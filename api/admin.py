from django.contrib import admin
from api.models import Category, BlogPost, Tag

admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(Tag)
