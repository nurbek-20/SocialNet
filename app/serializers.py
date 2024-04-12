from rest_framework import serializers
from .models import Comment, Like, FavoriteCollection, Favorite, Subscription, Post, File


class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class LikeListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        fields = ('id', 'user', 'post')


class LikeCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        fields = ('id', 'user', 'post')


class PostListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    files = FileListSerializer(many=True)

    class Meta:
        model = Post
        fields = ('user', 'files')


class PostCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('id', 'user', 'files', 'description', 'created_at')


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('id', 'user', 'post', 'content')


class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('id', 'user', 'post', 'content')


class FavoriteListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Favorite
        fields = ('id', 'user', 'post', 'favorite_collection')


class FavoriteCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Favorite
        fields = ('id', 'user', 'post', 'favorite_collection', )


class FavoriteCollectionListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FavoriteCollection
        fields = ('id', 'user', 'title')

    def validate_favorite_collection(self, value):
        user = self.context['request'].user
        if value.user != user:
            raise serializers.ValidationError("Вы не можете добавить пост в коллекцию, которую не создали.")
        return value


class FavoriteCollectionCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FavoriteCollection
        fields = ('id', 'user', 'title', )


class SubscriptionListSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Subscription
        fields = ('id', 'user', 'target_user')

    def get_queryset(self):
        user = self.request.user
        return Subscription.objects.filter(user=user)


class SubscriptionCreateSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Subscription
        fields = ('id', 'user', 'target_user')

    def get_queryset(self):
        user = self.request.user
        return Subscription.objects.filter(user=user)