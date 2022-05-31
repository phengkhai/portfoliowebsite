from django.urls import path
from . import views
from .views import PostList

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.contact, name="contact"),
    path('',PostList.as_view(), name = "post-home"),
]