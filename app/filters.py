from django_filters import rest_framework as filters
from .models import Post, Favorite, Subscription


class PostFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['user', 'description']


class FavoriteFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Favorite
        fields = ['favorite_collection__title', ]


class SubscriptionFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Subscription
        fields = ['target_user', ]