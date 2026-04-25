from django import forms

class SchoolRegistrationForm(forms.Form):
    school_name = forms.CharField(max_length=100, label="School Name")
    subdomain = forms.CharField(max_length=50, label="Desired Subdomain (e.g., 'greenwood')")