from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response, APIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    ListAPIView
)

from .serializers import (
    PostListSerializer,
    PostCreateSerializer,
    CommentCreateSerializer,
    CommentListSerializer,
    LikeListSerializer,
    LikeCreateSerializer,
    FavoriteListSerializer,
    FavoriteCreateSerializer,
    FavoriteCollectionListSerializer,
    FavoriteCollectionCreateSerializer,
    SubscriptionListSerializers,
    SubscriptionCreateSerializers,
)

from .models import (
    Comment,
    Like,
    FavoriteCollection,
    Favorite,
    Subscription,
    Post)

from .filters import PostFilter, SubscriptionFilter, FavoriteFilter
from .paginations import PostPagination


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostPagination
    filterset_class = PostFilter
    search_fields = ['description',]
    ordering_fields = ['created_at', ]


class PostCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


class PostDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


class PostUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def check_object_permissions(self, request, obj):
        if obj.user != request.user:
            raise PermissionDenied("У вас не прав для редактирования данного поста.")


class PostDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def check_object_permissions(self, request, obj):
        if obj.user != request.user:
            raise PermissionDenied("У вас не прав для редактирования данного поста.")


class LikedPostsListView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = PostPagination

    def get(self, request):
        user = request.user
        liked_posts = Like.objects.filter(user=user)
        serializer = LikeListSerializer(liked_posts, many=True)
        return Response(serializer.data)


class LikedPostsCreate(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = LikeCreateSerializer


class LikedPostsDelete(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = LikeCreateSerializer

    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)

# class CommentListView(ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = CommentListSerializer
#     lookup_field = 'pk'
#
#     def get_queryset(self):
#         post_pk = self.kwargs.get(self.lookup_field)
#         return Comment.objects.filter(pk=post_pk)


class CommentListView(ListAPIView):
    serializer_class = CommentListSerializer
    pagination_class = PostPagination
    ordering_fields = ['created_at', ]

    def get_queryset(self):
        post_pk = self.kwargs.get('pk')
        return Comment.objects.filter(post_id=post_pk)


class CommentCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer


class CommentUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def get_object(self):
        return Comment.objects.get(pk=self.kwargs['pk'])

    # def check_object_permissions(self, request, obj):
    #     if obj.author != request.user:
    #         raise PermissionDenied("У вас не прав для редактирования данного комментария.")


class CommentDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)


class FavoriteListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteListSerializer
    pagination_class = PostPagination
    filterset_class = FavoriteFilter
    search_fields = ['favorite_collection__title', ]
    ordering_fields = ['created_at', ]

    def get_queryset(self):
        user = self.request.user
        return Favorite.objects.filter(user=user)


class FavoriteCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteCreateSerializer


class FavoriteUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteCreateSerializer

    def get_object(self):
        return Favorite.objects.get(pk=self.kwargs['pk'])

    # def check_object_permissions(self, request, obj):
    #     if obj.user != request.user:
    #         raise PermissionDenied("У вас не прав для редактирования .")


class FavoriteDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteCreateSerializer


class FavoriteCollectionListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FavoriteCollection.objects.all()
    serializer_class = FavoriteCollectionListSerializer
    pagination_class = PostPagination
    ordering_fields = ['created_at', ]

    def get_queryset(self):
        user = self.request.user
        return FavoriteCollection.objects.filter(user=user)


class FavoriteCollectionCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FavoriteCollection.objects.all()
    serializer_class = FavoriteCollectionCreateSerializer

    def get_queryset(self):
        user = self.request.user
        return FavoriteCollection.objects.filter(user=user)


class FavoriteCollectionUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FavoriteCollection.objects.all()
    serializer_class = FavoriteCollectionCreateSerializer

    def get_queryset(self):
        user = self.request.user
        return FavoriteCollection.objects.filter(user=user)

    def check_object_permissions(self, request, obj):
        if obj.user != request.user:
            raise PermissionDenied("У вас не прав для редактирования.")


class FavoriteCollectionDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FavoriteCollection.objects.all()
    serializer_class = FavoriteCollectionCreateSerializer

    def get_queryset(self):
        user = self.request.user
        return FavoriteCollection.objects.filter(user=user)


class SubscriptionListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionListSerializers
    pagination_class = PostPagination
    filterset_class = SubscriptionFilter
    search_fields = ['target_user', ]
    ordering_fields = ['created_at', ]

    def get_queryset(self):
        user = self.request.user
        return Subscription.objects.filter(user=user)


class SubscriptionCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionCreateSerializers


class SubscriptionDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionCreateSerializers

    def check_object_permissions(self, request, obj):
        if obj.user != request.user:
            raise PermissionDenied("У вас не прав для редактирования.")


class NewsFeedView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostListSerializer

    def get_queryset(self):
        user = self.request.user
        subscribed_users = user.subscriptions.all().values_list('target_user', flat=True)
        return Post.objects.filter(user__in=subscribed_users)