from django.shortcuts import render
from django.db.models import Q

from Post.models import Post
from .serializers import PostListAPISerializer, PostAPISerializer
from .permissions import IsOwnerOrReadOnly
from .pagination import PagePagination, PageLimitPagination

from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostListAPISerializer
    queryset = Post.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "content"]
    ordering_fields = "__all__"
    pagination_class = PagePagination
    # permission_classes = [AllowAny]

    # def get_queryset(self, *arg, **kwargs):
    #     queryset_list = Post.objects.all()
    #     query = self.request.GET.get("q")
    #     if query:
    #         queryset_list = queryset_list.filter(
    #                                             Q(title__icontains=query)|
    #                                             Q(content__icontain=query)|
    #                                             Q(user__first__icontains=query)
    #                                             ).first()
    #     return queryset_list


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostAPISerializer
    # permission_classes = [AllowAny,]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class PostDetailAPIView(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostAPISerializer
    lookup_field = "slug"


class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostAPISerializer
    lookup_field = "slug"
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


# class PostDeleteAPIView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostListAPISerializer
#     lookup_field = 'slug'
