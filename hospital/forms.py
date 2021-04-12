from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username','email', 'gender', 'phonenumber', 'address', 'bloodgroup')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','email', 'gender', 'phonenumber', 'address', 'bloodgroup')
