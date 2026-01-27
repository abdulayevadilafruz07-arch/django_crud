from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListView.as_view(), name='index'),
    path('create/',views.CreateCountry.as_view(), name='create'),
    path('detail/<int:pk>',views.DetailView.as_view(), name='detail'),
    path('update/<int:pk>',views.UpdateCountry.as_view(), name='update'),
    path('delete/<int:pk>',views.DeleteCountry.as_view(), name='delete'),
]
