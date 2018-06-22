from django import forms
from .models import Student

class EmailSignupForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('name','email',)
    
