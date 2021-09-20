from django.urls import path
from .views import Blog, PostDetail, CatListView

urlpatterns = [
    path('', Blog, name='blog'),
    path('<slug:post>/', PostDetail, name='PostDetail'),
    path('category/<category>', CatListView.as_view(), name='category')
]