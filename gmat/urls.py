from django.urls import path
from . import views

urlpatterns = [
    path('', views.gmat_list, name='gmat_list'),
]