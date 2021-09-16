from django.shortcuts import render
from .models import Post

# Create your views here.

#Blog
def Blog(request):
    
    all_posts = Post.objects.all() #collected all data from post model
    return render(request, 'blog.html', {'posts': all_posts})

#Front end assets 
def FrontEnd(request):
    return render(request, 'frontend.html')