from django.urls import path
from .views import get_all

urlpatterns = [
    path("",view=get_all, name="git_all")
]
