from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api import views

router = DefaultRouter()
router.register('stream', views.StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    # path('list/', views.movie_list, name='movie-list'),
    # path('<int:pk>', views.movie_details, name='movie-details'),

    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name='movie-details'),
    path('list2/', views.WatchListGV.as_view(), name='watch-list'),

    path('', include(router.urls)),

    # path('stream/', views.StreamPlatformAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>', views.StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),

    # path('review/', views.ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', views.ReviewDetail.as_view(), name='review-detail'),

    # path('stream/<int:pk>/review-create/', views.ReviewCreate.as_view(), name='review-create'),
    # path('stream/<int:pk>/review/', views.ReviewList.as_view(), name='review-list'),
    # path('stream/review/<int:pk>', views.ReviewDetail.as_view(), name='review-detail'),

    path('<int:pk>/review-create/', views.ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', views.ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),

    path('reviews/', views.UserReview.as_view(), name='user-review-detail'),
]
