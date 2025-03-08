from django.urls import path
from .views import base,blogs,detail

app_name = 'main'

urlpatterns = [
    path('',base, name='base'),
    path('blogs/',blogs,name='blogs'),
    path('blogs/<int:pk>/',detail, name='detail')
]