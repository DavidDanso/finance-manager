from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('manage-users/', views.user_management, name='users'),
    path('download_report/<str:report_id>', views.download_report, name='download_report'),
]
