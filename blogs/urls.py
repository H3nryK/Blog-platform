from django.urls import path
from .views import *

urlpatterns = [
    path('', upload_blogs, name='uploads'),
    path('blogs/', list_blogs, name='blogs'),
    path('blogs/<int:blog_id>/', detail_blogs, name='blog-detail'),
]
