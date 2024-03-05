from django.urls import path
from .views import PostList, PostDetail
urlpatterns = [
  path('careers/', PostList.as_view()),
  path('careers/<int:pk>/', PostDetail.as_view())
]
