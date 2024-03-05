from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, PostCreateSerializer,PostUpdateSerializer

class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  
  def get_serializer_class(self):
    if self.request.method == 'POST':
      return PostCreateSerializer
    return self.serializer_class
  
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class=PostSerializer

  def get_serializer_class(self):
    if self.request.method == 'PATCH':
      return PostUpdateSerializer
    return self.serializer_class