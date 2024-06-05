from django import forms
import django_filters
from .models import Report
from accounts.models import Profile
from django_filters import DateFilter

class ReportFilter(django_filters.FilterSet):
    username = django_filters.ModelChoiceFilter(
        field_name='account_owner',
        queryset=Profile.objects.all(),
        label='Username',
        to_field_name='username'
    )

    created = DateFilter(
        field_name='created_time_stamp',
        lookup_expr='date',
        label='Date',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = Report
        fields = ['username', 'created']
