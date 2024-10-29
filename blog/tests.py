from django.test import TestCase
from django.shortcuts import reverse
from .models import *
from django.contrib.auth.models import User

class BlogPostTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username = 'hasan'
        )


        self.post1 = Post.objects.create(
            title = 'post1',
            text = 'some test text for this post',
            author = self.user,
            
        )

        self.post2 = Post.objects.create(
            title = 'post2',
            text = 'some other test text in post2',
            author = self.user,
            published = True
        )


    def test_posts_list_by_url(self):

        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_posts_list_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_posts_list_page(self):
        response = self.client.get('/posts/')
        self.assertContains(response, self.post2.title)

    def test_post_detail_by_url(self):
        response = self.client.get(f'/posts/{self.post2.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))

    def test_post_title_on_detail_page(self):
        response = self.client.get(f'/posts/{self.post2.id}/')
        self.assertContains(response, self.post2.title)
        self.assertContains(response, self.post2.text)

    def test_status_404_if_post_dose_not_exists(self):
        response = self.client.get(reverse('post_detail', args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_draft_posts_in_list(self):
        response = self.client.get('/posts/')
        self.assertContains(response, self.post2.title)
        self.assertNotContains(response, self.post1.title)




