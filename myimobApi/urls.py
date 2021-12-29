from django.urls import path
from .views import get_all,apiOverview

urlpatterns = [
    path("",view=apiOverview, name="apiOverview"),
    path("house_list/",view=get_all,name="get_all"),
]
