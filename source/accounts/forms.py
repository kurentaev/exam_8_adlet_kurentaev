from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label="Login"
    )
    password = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput
    )
    next = forms.CharField(
        required=False,
        widget=forms.HiddenInput
    )


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )
    password_confirm = forms.CharField(
        label="Password confirm",
        required=True,
        widget=forms.PasswordInput,
        strip=False
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Passwords dont match!')
        if len(last_name) == 0:
            raise forms.ValidationError('Last name field is required')
        if len(email) == 0:
            raise forms.ValidationError('Email field is required')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username',
                  'password',
                  'password_confirm',
                  'first_name',
                  'last_name',
                  'email'
                  )


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  )
        labels = {'username': 'Username',
                  'first_name': 'First name',
                  'last_name': 'Last name',
                  'email': 'Email',
                  }


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(
        label="New password",
        strip=False,
        widget=forms.PasswordInput
    )
    password_confirm = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput,
        strip=False
    )
    old_password = forms.CharField(
        label="Old password",
        strip=False,
        widget=forms.PasswordInput
    )

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Password dont match!')
        return password_confirm

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Old password incorrect!')
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['password', 'password_confirm', 'old_password']
