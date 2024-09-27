from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post


class PostTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            email="test@gmail.com", username="testuser", password="pass"
        )
        cls.post = Post.objects.create(
            title="A good title",
            body="Nice body content",
            auther=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(self.post.auther.username, "testuser")
        self.assertEqual(str(self.post), "A good title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")
