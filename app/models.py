from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import ValidationError

User = get_user_model()


class File(models.Model):
    file = models.FileField(upload_to='media/post/detail_file')


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )
    description = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    files = models.ManyToManyField(File)

    def formatted_created_at(self):
        return self.created_at.strftime('%d-%m-%Y, %H:%M')

    def __str__(self):
        return self.description


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def formatted_created_at(self):
        return self.created_at.strftime('%d-%m-%Y, %H:%M')

    def __str__(self):
        return self.content


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ['user', 'post']


class FavoriteCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['user', 'title']


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    favorite_collection = models.ForeignKey(FavoriteCollection, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def formatted_created_at(self):
        return self.created_at.strftime('%d-%m-%Y, %H:%M')

    class Meta:
        unique_together = ['user', 'post', 'favorite_collection']


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='subscriptions')
    target_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='subscribers')
    created_at = models.DateTimeField(auto_now_add=True)

    def formatted_created_at(self):
        return self.created_at.strftime('%d-%m-%Y, %H:%M')

    class Meta:
        unique_together = ['user', 'target_user']

