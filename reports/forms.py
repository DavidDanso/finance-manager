from django import forms
from django.forms import ModelForm
from .models import *

# Upload Reports form
class UploadFileForm(forms.Form):
    file = forms.FileField()


# Report Creation form
class ReportCreationForm(ModelForm):
    class Meta:
        model = Report
        fields = ['description', 'main_category', 'sub_category', 'payment', 'report_note']
        exculde = ['account_owner', 'status', 'updated_time_stamp', 'created_time_stamp', 'id']
        # add id and placeholder to the input field
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'enter descriptiony here...', 'rows': 3, 'cols': 40}),
            'main_category': forms.TextInput(attrs={'placeholder': 'enter main category...'}),
            'sub_category': forms.TextInput(attrs={'placeholder': 'enter sub category...'}),
            'report_note': forms.Textarea(attrs={'placeholder': 'enter report here...', 'rows': 3, 'cols': 40}),
        }
    # add class to the input field
    def __init__(self, *args, **kwargs):
        super(ReportCreationForm, self).__init__(*args, **kwargs)
        for name, fields in self.fields.items():
            fields.widget.attrs.update({'class': 'input form-control'})



class ReportEditForm(ModelForm):
    class Meta:
        model = Report
        fields = ['description', 'main_category', 'sub_category', 'payment', 'status', 'report_note']
        exculde = ['account_owner', 'updated_time_stamp', 'created_time_stamp', 'id']
        # add id and placeholder to the input field
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'enter descriptiony here...', 'rows': 3, 'cols': 40}),
            'main_category': forms.TextInput(attrs={'placeholder': 'enter main category...'}),
            'sub_category': forms.TextInput(attrs={'placeholder': 'enter sub category...'}),
            'report_note': forms.Textarea(attrs={'placeholder': 'enter report here...', 'rows': 3, 'cols': 40}),
        }
    # add class to the input field
    def __init__(self, *args, **kwargs):
        super(ReportEditForm, self).__init__(*args, **kwargs)
        for name, fields in self.fields.items():
            fields.widget.attrs.update({'class': 'input form-control'})

