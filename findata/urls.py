from django.urls import path
from . import views

urlpatterns = [
    path("", views.findata_home, name='findata_home'),
    path("statistic/", views.findata_statistic, name='findata_statistic')
]
