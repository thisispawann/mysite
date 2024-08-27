from django.urls import path
from .views import Blog, PostDetail, CatListView, AllEntries, Projects, Certificates, About

urlpatterns = [
    path('', Blog, name='blog'),
    path('about/', About, name='About'),
    path('allEntries/', AllEntries, name='AllEntries'),
    path('projects/', Projects, name = 'Projects'),
    path('certificates/', Certificates, name = 'Certificates'),
    path('<slug:post>/', PostDetail, name='PostDetail'),
    path('category/<category>', CatListView.as_view(), name='category')
    
]