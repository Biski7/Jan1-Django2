from django import forms
from django.core import validators

# MAKING OWN CUSTOM VALIDATION
def check_for_a(value):
    if value[0].lower() != 'a':
        raise forms.ValidationError('Name needs to start with a or A')

class Form_1(forms.Form):
    name = forms.CharField(validators=[check_for_a])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter email address again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators = [validators.MaxLengthValidator(0)])

    # Cleaning all fields at once
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_email = all_clean_data['verify_email']
        
        # Checking if email matches
        if email!= v_email:
            raise forms.ValidationError('Email did not match')


