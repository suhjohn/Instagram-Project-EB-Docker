# PostList를 리턴하는 APIView
from django.http import Http404
from rest_framework import status, generics
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    query = Post.objects.all()
    serializer_class = PostSerializer
