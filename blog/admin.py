from django.contrib import admin
from .models import Article, Category, Tag, Nav, NavCollapse, Links, BlogSettings, Log

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Nav)
admin.site.register(BlogSettings)
admin.site.register(Links)
admin.site.register(Log)
