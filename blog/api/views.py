from blog.api.serializers import PostSerializer
from blog.models import Post
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication


class PostList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
