from django import forms

class ApplicationForm(forms.Form):
    full_name = forms.CharField(max_length=80)
    phone = forms.CharField(max_length=80)
    national_id = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(max_length=50)

