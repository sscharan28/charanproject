from django import forms
from .models import Dashboard

class Regform(forms.Form):
    FirstName = forms.CharField(max_length=10)
    LastName = forms.CharField(max_length=10)
    UserName = forms.CharField(max_length=10)
    Password = forms.CharField(max_length=10, widget=forms.PasswordInput())
    CPassword = forms.CharField(max_length=10, widget=forms.PasswordInput())
    EmailId = forms.EmailField()
    MobileNumber = forms.IntegerField()
class Loginform(forms.Form):
    UserName = forms.CharField(max_length=10)
    Password = forms.CharField(max_length=10, widget=forms.PasswordInput())

class Taskform(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = [
            "title",
            "description",
        ]