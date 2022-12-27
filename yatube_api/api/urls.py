from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

app_name = 'api'

v1_router = DefaultRouter()

v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)
v1_router.register('follow', FollowViewSet, basename='follow')
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename='comment')

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(v1_router.urls), name='api_v1'),
]
