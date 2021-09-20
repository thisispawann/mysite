from django.urls import path
from .views import Blog, PostDetail

urlpatterns = [
    path('', Blog, name='blog'),
    path('<slug:post>/', PostDetail, name='PostDetail'),
]