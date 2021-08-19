from django.shortcuts import render
from .models import Post
# Create your views here.

#List all the posts

def post_list_view(request):
  post_objects = Post.objects.all()
  context = {
    'post_objects': post_objects
  }
  return render(request, "index.html", context)