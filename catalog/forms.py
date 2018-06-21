from django import forms

class EmailSignupForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
