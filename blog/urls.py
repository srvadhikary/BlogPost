from django.urls import path
from .views import list_blogs,create_blog,update_blog,delete_blog
#from . import views

urlpatterns = [
    path('', list_blogs, name='list_blogs'),
    path('new', create_blog, name='create_blog'),
    path('update/<int:id>', update_blog, name='update_blog'),
    path('delete/<int:id>', delete_blog, name='delete_blog'),
]
