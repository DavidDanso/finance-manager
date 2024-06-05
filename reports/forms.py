from django import forms
from django.forms import ModelForm
from .models import *


# Client Creation form
class ReportCreationForm(ModelForm):
    class Meta:
        model = Report
        fields = ['description', 'main_category', 'sub_category', 'payment']
        exculde = ['account_owner', 'status', 'updated_time_stamp', 'created_time_stamp', 'id']
        # add id and placeholder to the input field
        widgets = {
            'description': forms.TextInput(attrs={'placeholder': 'enter descriptiony here...'}),
            'main_category': forms.TextInput(attrs={'placeholder': 'enter main category...'}),
            'sub_category': forms.TextInput(attrs={'placeholder': 'enter sub category...'}),
            'payment': forms.TextInput(attrs={'placeholder': 'enter payment...'}),
        }
    # add class to the input field
    def __init__(self, *args, **kwargs):
        super(ReportCreationForm, self).__init__(*args, **kwargs)
        for name, fields in self.fields.items():
            fields.widget.attrs.update({'class': 'input form-control'})




    

