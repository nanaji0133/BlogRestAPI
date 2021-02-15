from django.urls import path
from Post.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', PostListAPIView.as_view(), name='post-list'),
    #path('<slug>/', PostListAPIView.as_view(), name='post-list'),
    path('create/', PostCreateAPIView.as_view(), name='post-create'),
    path('<slug>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('<slug>/edit/', PostUpdateAPIView.as_view(), name='post-update'),
    # path('<slug>/delete/', PostDeleteAPIView.as_view(), name='post-delete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)