from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('verify_email/', views.Verify_EmailView.as_view(), name='verify_email'),
]