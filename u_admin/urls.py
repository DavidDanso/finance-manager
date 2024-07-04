from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='dashboard'),
    path('manage-users/', views.user_management, name='users'),
    path('download_report/<str:report_id>', views.download_report, name='download_report'),
    path('edit-user/<str:pk>', views.update_user, name='edit-user'),

    path('review-report/<str:report_id>', views.review_report, name='review-report'),
    path('edit-report/<str:pk>', views.edit_report, name='report-edit'),
    path('pending-reports', views.pending_reports, name='pending-reports'),
]
