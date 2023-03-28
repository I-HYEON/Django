from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from django import forms

class CustomUserCreationForm(UserCreationForm):
    phone_number = PhoneNumberField()

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('phone_number',)
        

class CustomUserChangeForm(UserChangeForm):
    phone_number = PhoneNumberField()
    
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username','email','phone_number',)