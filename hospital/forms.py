from django import forms
from .models import User, Appointment
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'gender', 'address', 'bloodgroup')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'gender', 'address', 'bloodgroup')

    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
        'patientemail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email'}),
        'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        'phonenumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pick Appointment time'}),
        'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Symtoms here'}),
        'bloodgroup': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Details of your prescription'})
    }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctorname', 'doctoremail', 'patientname', 'patientemail', 'symptoms', 'prescription',
                  'appointmentdate', 'appointmenttime']
        labels: {
            'doctorname': '',
            'doctoremail': '',
            'patientname': '',
            'patientemail': '',
            'appointmentdate': '',
            'appointmenttime': '',
            'symptoms': '',
            'prescription': ''

        }

        class DateInput(forms.DateInput):
            input_type = 'date'

        class TimeInput(forms.TimeInput):
            input_type = 'time'

        input_formats = ['%d/%m/%Y %H:%M']
        widgets = {
            'doctorname': forms.Select(attrs={'class': 'form-control'}),
            'doctoremail': forms.Select(attrs={'class': 'form-control'}),
            'patientname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'patientemail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email'}),
            'symptoms': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Symtoms here'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'prescription': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Details of your prescription'}),
            'appointmentdate': DateInput(),
            'appointmenttime': TimeInput(),
        }
