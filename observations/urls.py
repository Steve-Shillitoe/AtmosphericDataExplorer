from django.urls import path
from . import views

urlpatterns = [
    path('', views.observation_list, name='observation_list'),
]

