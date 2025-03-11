from django import forms
from captcha.fields import CaptchaField
from .models import Doctor

class DoctorRegistrationForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Doctor
        fields = '__all__' 
       
    profile_picture = forms.ImageField(required=False)
