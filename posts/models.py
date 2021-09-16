from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='publish')
    publish = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=255, choices=options, default='draft')
    
    
    #showing only date
    def datepublished(self):
        return self.date_publish.strftime('%B %d %Y')
    
    
    #showing post by order
    class Meta:
        ordering = ('-publish',)
    
    
    #showing title to the admin panel
    def __str__(self):
        return self.title
    