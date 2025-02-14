from django.urls import path
from .views import index,blogs,details
app_name = "main"

urlpatterns = [
    path("", index, name="index"),
    path("blogs/",blogs,name="blogs"),
    path("blogs/<int:pk>",details, name="detayle")
]