from django.urls import path
from .views import Blog, PostDetail, CatListView, AllEntries, Projects, Certificates

urlpatterns = [
    path('', Blog, name='blog'),
    path('allEntries/', AllEntries, name='AllEntries'),
    path('projects/', Projects, name = 'Projects'),
    path('certificates/', Certificates, name = 'Certificates'),
    path('<slug:post>/', PostDetail, name='PostDetail'),
    path('category/<category>', CatListView.as_view(), name='category')
    
]