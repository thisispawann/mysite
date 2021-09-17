from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

#Blog
def Blog(request):
    all_posts = Post.newmanager.all() #collected all data from post model
    return render(request, 'blog.html', {'posts': all_posts})

#post detail
def PostDetail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'post_detail.html', {'post': post})