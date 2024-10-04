from django import forms
from .models import Report
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['location', 'gps_coordinates', 'description', 'mining_type', 'photo', 'reporter_contact']

    gps_coordinates = forms.CharField(widget=forms.HiddenInput(), required=False)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=255, required=True, label='Search by Location')
