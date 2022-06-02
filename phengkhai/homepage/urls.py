from django.urls import path
from . import views
from .views import WrapperView

urlpatterns = [
        path('', WrapperView.as_view(), name = "home"),
]