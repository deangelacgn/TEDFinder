from django import forms
from django.forms.models import modelformset_factory, inlineformset_factory
from django.forms import ValidationError, ModelForm, Form, Textarea, TextInput, CheckboxInput, DateInput
from django.forms.widgets import ClearableFileInput

class LoginForm(Form):
    username = forms.CharField(
        label='E-mail',
        min_length=5,
        max_length=50,
        error_messages={
            'required':"Informe um endereço de e-mail válido!"
        },
        widget = forms.TextInput(
            attrs = {
                'class': "form-control",
                'placeholder': 'username'
                }
            )
        )
    password = forms.CharField(
        label = 'Senha',
        min_length = 6,
        max_length = 30,
        error_messages = {
            'required': 'A senha é obrigatória!'
        },
        widget = forms.PasswordInput(
            attrs = {
                'class': "form-control",
                'placeholder': '**********'
                }
            )
        )
