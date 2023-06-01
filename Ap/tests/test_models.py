from django.test import TestCase
from Ap.models import Post
from django.contrib.auth.models import User

# class TestPostModel(TestCase):   
#     def test_post(self):
#         tytul = Post.objects.create(tytul= "test")
#         autor = Post.objects.create(autor= "gabi")
#         tresc = Post.objects.create(tresc = "piekny dzien")
#         data = Post.objects.create(data = "2021-01-01")
#         self.assertEqual(str(tytul), "test")

# def setUpTestData(TestCase):
#     user = User.objects.create(username="gaba")
#     Post.objects.create(NewsLetterID=1, Email='test@test.com', Connected=False,UserID=user)