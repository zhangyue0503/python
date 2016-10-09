from django.shortcuts import render,render_to_response
from datetime import datetime
from blog.models import BlogPost,BlogPostForm
from django.template import loader,Context,RequestContext
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt
from django.views.generic.simple import direct_to_template
# Create your views here.

def archive(request):
    posts = BlogPost.objects.all()[:10]
    return render_to_response('archive.html',{'posts':posts,'form':BlogPostForm()})
@csrf_exempt
def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = datetime.now()
            post.save()
        # BlogPost(
        #     title = request.POST.get('title'),
        #     body = request.POST.get('body'),
        #     timestamp = datetime.now()
        # ).save()
        return HttpResponseRedirect('/blog')