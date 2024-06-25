from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.accountant_dashboard, name='a_dashboard'),
    path('reports', views.create_report, name='reports'),
    path('download_report/<str:report_id>', views.download_report, name='download_report'),
    path('upload/', views.upload_file, name='upload_file'),
    path('edit-report/<str:pk>', views.edit_report, name='edit-report'),
    path('corrections', views.corrections_page, name='corrections'),
    path('correction_done/<str:report_id>', views.correction_status, name='correction_done'),
]