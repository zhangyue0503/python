from django.test import TestCase
from datetime import datetime
from django.test import TestCase
from django.test.client import Client
from blog.models import BlogPost

# Create your tests here.
class BlogPostTest(TestCase):
    def test_obj_create(self):
        BlogPost.objects.create(title='raw title',
                                body='raw body',timestamp=datetime.now())
        