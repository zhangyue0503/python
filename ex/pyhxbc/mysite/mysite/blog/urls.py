#!/usr/bin/env python
from django.conf.urls import *
import blog.views

urlpatterns = [
    url(r'^$',blog.views.archive),
    url(r'^create/',blog.views.create_blogpost)
    # url(r'foo/',blog.views.foo),
    # url(r'bar/',blog.views.bar),
]