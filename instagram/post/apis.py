# PostList를 리턴하는 APIView
from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from member.serializers import UserSerializer
from .models import Post
from .serializers import PostSerializer
from utils.permissions import *


# class PostList(APIView):
#
#     def get(self, request):
#         post = Post.objects.all()
#         serializer = PostSerializer(post, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if request.user and serializer.is_valid():
#             serializer.save(
#                 author=request.user,
#             )
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        # author 가 아니면 지울 수 없도록 utils.permissions
        IsAuthorOrReadOnly,
    )


class PostLikeToggle(generics.GenericAPIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    queryset = Post.objects.all()

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if user.like_posts.filter(pk=instance.pk):
            user.like_posts.remove(instance)
            like_status = False
        else:
            user.like_posts.add(instance)
            like_status = True
        data = {
            'user': UserSerializer(user).data,
            'post': PostSerializer(instance).data,
            'like_status': like_status,
         }
        return Response(data)
