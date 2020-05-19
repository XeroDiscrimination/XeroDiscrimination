from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    username = forms.CharField(label="Username", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username",'autofocus': ''}))
    password = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control',  'placeholder': "Password"}))
    captcha = CaptchaField(label='Captcha')

class RegisterForm(forms.Form):
    pronouns = (
        ('they', "They/Them"),
        ('he', "He/Him"),
        ('she', "She/Her"),
        ('ot', 'Other'),
        ('na', "Rather not say"),
    )

    username = forms.CharField(label="Username", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email address", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    pronoun = forms.ChoiceField(label='Pronouns', choices=pronouns)
    captcha = CaptchaField(label='Captcha')