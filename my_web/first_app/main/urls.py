from django.urls import path
from .views import index,blog,index_2

app_name = "main"

urlpatterns = [
    path("", index, name="index"),
    path('blog/', blog, name='blog'),
    path("index_2/",index_2,name="index_2")
]