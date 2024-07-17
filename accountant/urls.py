from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.accountant_dashboard, name='a_dashboard'),
    path('reports', views.create_report, name='reports'),
    path('download_report/<str:report_id>', views.download_report, name='download_report'),
    path('upload/', views.upload_file, name='upload_file'),
    path('corrections', views.corrections_page, name='corrections'),
    path('make-correction/<str:report_id>', views.make_correction, name='make-correction'),
    path('report/<str:report_id>', views.report_update, name='report'),
]