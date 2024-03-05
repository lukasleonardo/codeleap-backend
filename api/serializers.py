from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model=Post
    fields=('__all__')
    
class PostCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model=Post
    fields=('username','title','content')
    
    def validate_username(self, value):
        if not value:
            raise serializers.ValidationError("O campo 'username' não pode estar vazio.")
        return value

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("O campo 'title' não pode estar vazio.")
        return value

    
class PostUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model=Post
    fields=('title','content')
    
    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("O campo 'title' não pode estar vazio.")
        return value

    def validate_content(self, value):
        if not value:
            raise serializers.ValidationError("O campo 'content' não pode estar vazio.")
        return value