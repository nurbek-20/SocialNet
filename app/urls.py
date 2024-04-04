from django.urls import path
from . import views

urlpatterns = [
    path('post_list/', views.PostListView.as_view()),
    path('post_create/', views.PostCreateView.as_view()),
    path('post_detail/<int:pk>/', views.PostDetailView.as_view()),
    path('post_update/<int:pk>/', views.PostUpdateView.as_view()),
    path('post_delete/<int:pk>/', views.PostDeleteView.as_view()),

    path('liked_posts_list/', views.LikedPostsListView.as_view()),
    path('liked_posts_create/', views.LikedPostsCreate.as_view()),
    path('liked_posts_delete/<int:pk>/', views.LikedPostsDelete.as_view()),

    path('comment_list/<int:pk>/', views.CommentListView.as_view()),
    path('comment_create/', views.CommentCreateView.as_view()),
    path('comment_update/<int:pk>/', views.CommentUpdateView.as_view()),
    path('comment_delete/<int:pk>/', views.CommentDeleteView.as_view()),

    path('favorite_list/', views.FavoriteListView.as_view()),
    path('favorite_create/', views.FavoriteCreateView.as_view()),
    path('favorite_update/<int:pk>/', views.FavoriteUpdateView.as_view()),
    path('favorite_delete/<int:pk>/', views.FavoriteDeleteView.as_view()),

    path('favorite_collection_list/', views.FavoriteCollectionListView.as_view()),
    path('favorite_collection_create/', views.FavoriteCollectionCreateView.as_view()),
    path('favorite_collection_update/<int:pk>/', views.FavoriteCollectionUpdateView.as_view()),
    path('favorite_collection_delete/<int:pk>/', views.FavoriteCollectionDeleteView.as_view()),

    path('subscription_list/', views.SubscriptionListView.as_view()),
    path('subscription_create/', views.SubscriptionCreateView.as_view()),
    path('subscription_delete/<int:pk>/', views.SubscriptionDeleteView.as_view()),
    path('news_feed_list', views.NewsFeedView.as_view()),

]
