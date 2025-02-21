from django.urls import path
from .views import index,blog,index_2,single_blog,flighter,team,elements,content

app_name = "main"

urlpatterns = [
    path("", index, name="index"),
    path('blog/', blog, name='blog'),
    path("index_2/",index_2,name="index_2"),
    path('singe_blog/',single_blog, name="single-blog"),
    path('flighter/', flighter, name="flighter"),
    path('team/',team,name="team"),
    path('elements/', elements, name="elements"),
    path('content/', content, name="content"),
]