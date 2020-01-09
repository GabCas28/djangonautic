from django import forms

class NameForm(forms.Form)
    yout_name = forms.CharField(label='Your name', max_length=100)