from django import forms
from jobPortalApp.models import *

class JobForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = "__all__"
        exclude = ['CreatedBy']
        
        widgets = {
            'deadline':forms.DateInput(attrs={
                'type': 'date'
            })
        }

class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = jobApplyModel
        fields = "__all__"
        exclude = ['applicant','job','status']
