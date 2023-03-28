from django.contrib.auth.forms import UserCreationForm,UserChangeForm
# from .models import User
from django.contrib.auth import get_user_model
# from django import forms  # 이거 맞나?

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username','email',)