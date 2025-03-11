from django.urls import path
from .views import base,blogs,detail,create,delete

app_name = 'main'

urlpatterns = [
    path('',base, name='base'),
    path('blogs/',blogs,name='blogs'),
    path('blogs/<int:pk>/',detail, name='detail'),
    path('blogs/create',create, name='create'),
    path('blogs/delete/<int:pk>/',delete, name='delete')
]