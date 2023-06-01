from django.test import TestCase, Client
from django.urls import reverse
from Ap.models import Post


class TestAllPostsView(TestCase):   
    def setUp(self):
        self.client = Client()
        self.forum_url = reverse('forum')
            
    def test_forum_GET(self):
        response = self.client.get(self.forum_url)      
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Ap/forum.html')