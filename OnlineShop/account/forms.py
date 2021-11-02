from .models import User
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm_password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'full_name', 'mobile', 'address')
        labels = {'email': 'پست الکترونیکی','full_name': 'نام','mobile': 'تلفن همراه','address': 'آدرس'}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('passwords do not match')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model=User
        fields = ['email', 'password', 'full_name']
        labels = {'email': 'پست الکترونیکی', 'password': 'کلمه عبور', 'full_name': 'نام'}

        def clean_password(self):
            return self.initial['password']


class UserLoginForm(forms.Form):
    mobile = forms.CharField(label='موبایل', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegistrationForm(forms.Form):
    email = forms.EmailField(label='پست الکترونیکی', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    mobile = forms.CharField(label='موبایل', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='آدرس', widget=forms.TextInput(attrs={'class': 'form-control'}))
    full_name = forms.CharField(label='نام و نام خانوادگی', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class EditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'full_name', 'mobile', 'address')
        labels = {'email': 'پست الکترونیکی', 'full_name': 'نام', 'mobile': 'تلفن همراه', 'address': 'آدرس'}



