from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField, SerializerMethodField

from .models import Post

from Accounts.serializers import UsersSerializer

post_detail_url = HyperlinkedIdentityField(
    view_name='post-app:post-detail',   
    lookup_field = 'slug'
)

class PostListAPISerializer(serializers.ModelSerializer):
    url = post_detail_url
    user = UsersSerializer()
    class Meta:
        model = Post
        fields = ['url', 'id', 'user', 'title', 'slug', 'image', 'content',]

    # def get_user(self, obj):
    #     return f"{obj.user.username}"
        

class PostAPISerializer(serializers.ModelSerializer):
    url = post_detail_url
    class Meta:
        model = Post
        fields = ['url', 'id', 'user', 'title', 'slug', 'image', 'content',]

