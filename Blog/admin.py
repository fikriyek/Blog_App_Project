from django.contrib import admin
from .models import CategoryTable, Blog, Comment, PostViews, Likes 

# Register your models here.
admin.site.register(CategoryTable)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(PostViews)
admin.site.register(Likes)