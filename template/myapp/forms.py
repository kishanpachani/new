from django import forms
from .models import Signup,cart

class signupForm(forms.ModelForm):
    class Meta:
        model=Signup
        fields='__all__'

class cartform(forms.ModelForm):
    class Meta:
        model=cart
        fields = '__all__'