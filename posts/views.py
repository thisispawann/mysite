from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post, Category
from .forms import NewCommentForm
from django.views.generic import ListView

# Create your views here.
#Blog
def Blog(request):
    all_posts = Post.newmanager.all() #collected all data from post model
    return render(request, 'blog.html', {'posts': all_posts})

#post detail
def PostDetail(request, post):
    post = get_object_or_404(Post, slug=post, status='published') 
    #filtering out publish or not
    #slug=post is slug name goes to url like blog/slug
    comments = post.comments.filter(status=True)
    user_comment = None 
    
    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect("/" + post.slug)
    else:
        comment_form = NewCommentForm()
    return render(
        request,
        "post_detail.html",
        {
            "post": post,
            "comments": user_comment, 
            "comments":comments,
            "comment_form" : comment_form,
        }
    )
    
    
#Category Views
class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'
    
    def get_queryset(self):
        content = {
            'cat':self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(status='published') #filters the POST object by the name of category
        }
        return content


#Category List
def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list": category_list,
    }
    return context


def AllEntries(request):
    all_posts = Post.newmanager.all() #collected all data from post model
    return render(request, 'allEntries.html', {'posts': all_posts})

def Projects(request):
    return render(request,'projects.html')


def Certificates(request):
    return render(request,'certificates.html')