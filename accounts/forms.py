from django import forms
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm

class AccountForm(UserCreationForm):
    groups = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'groups' ]

    def save(self, commit=True):
        user = super().save(commit=False)
        print("hey")
        if commit:
            user.save()
        return user