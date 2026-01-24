from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateCountry.as_view(), name='create'),
    path('ListView/',views.ListView.as_view(), name='index'),
]
