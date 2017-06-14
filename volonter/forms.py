from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form):
    username = forms.CharField(label="Логін")
    email = forms.EmailField(label="Електронна пошта")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Повторіть пароль", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Введені паролі мають співпадати"
            )


class EventForm(forms.Form):
    name = forms.CharField(label="Назва події", max_length=100)
    description = forms.CharField(label="Опис події")
    contacts = forms.CharField(label="Контакти")
    image = forms.ImageField(label="Картинка для привернення уваги")


class OrganizationForm():
    pass


