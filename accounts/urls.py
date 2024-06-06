from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('profile', views.profilePage, name='profile'),
    path('logout', views.logoutPage, name='logout'),
]
