from django.urls import path
from . import views

urlpatterns = [
    path('reports', views.create_report, name='reports'),
    path('download_report/<str:report_id>', views.download_report, name='download_report'),
]