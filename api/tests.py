from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Post

class PostAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.model_data = {
            "username": "john_doe",
            "title": "Test Title",
            "content": "Test Content"
        }

    def test_create_model(self):
        response = self.client.post('/api/careers/', self.model_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().username, 'john_doe')

    def test_retrieve_model_list(self):
        Post.objects.create(**self.model_data)
        response = self.client.get('/api/careers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_model_detail(self):
        instance = Post.objects.create(**self.model_data)
        response = self.client.get(f'/api/careers/{instance.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'john_doe')

    def test_update_model(self):
        instance = Post.objects.create(**self.model_data)
        updated_data = {
            "title": "Updated Title",
            "content": "Updated Content"
        }
        response = self.client.patch(f'/api/careers/{instance.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.get(id=instance.id).title, 'Updated Title')

    def test_delete_model(self):
        instance = Post.objects.create(**self.model_data)
        response = self.client.delete(f'/api/careers/{instance.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)