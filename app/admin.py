from django.contrib import admin
from .models import Post, Subscription, FavoriteCollection, Favorite, Like, Comment, File


admin.site.register(Post)
admin.site.register(Subscription)
admin.site.register(FavoriteCollection)
admin.site.register(Favorite)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(File)