from django.urls import path
from .views import Blog, FrontEnd

urlpatterns = [
    path('', Blog, name='blog'),
    path('frontendcodes/', FrontEnd, name='frontend'),
]