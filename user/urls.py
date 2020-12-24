from django.urls import path
from user import views, services

urlpatterns = [
    path('', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('profile/', views.profile_page, name='profile'),
    path('logout/', services.logout, name='logout')
]
