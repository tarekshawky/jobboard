from django import forms
from .models import Apply, Job


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email', 'webiste', 'cv', 'cover_letter']
        


class JObForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title','description', 'location', 'job_type', 'vocancy', 'salary', 'experince', 'category' ,'image']