# resources.py
from import_export import resources
from .models import Report

class ReportResource(resources.ModelResource):
    class Meta:
        model = Report
        exclude = ('account_owner', 'updated_time_stamp', 'created_time_stamp', 'id')
        fields = ('description', 'main_category', 'sub_category', 'receipt', 'payment')