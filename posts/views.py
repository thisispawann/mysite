from django.shortcuts import render

# Create your views here.

#Blog
def Blog(request):
    return render(request, 'blog.html')

#Front end assets 
def FrontEnd(request):
    return render(request, 'frontend.html')