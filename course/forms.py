from django import forms
from course.models import User, Comment, Student
from course.authentiaction import AuthenticationForm
from django.db import models


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password2 = self.data.get('password2')
        if password2 != password:
            raise forms.ValidationError(f'Passwords did not match {password}, {password2}')
        return password2

    def clean_phone_number(self):
        phone_number = str(self.cleaned_data.get('phone_number'))
        if len(phone_number) != 13 and phone_number[0] != '+':
            raise forms.ValidationError('Invalid phone number')
        return phone_number

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    #  the difference between get and filter
    """ get() returns DoesNotExists when nothing is found,
        filter() returns None when nothing is found"""

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email does not exist')
        return email

    def clean_password(self):
        email = self.cleaned_data.get('email')
        password = self.data.get('password')
        try:
            user = User.objects.get(email=email)
            if not user.check_password(password):
                raise forms.ValidationError('Password did not match')
        except User.DoesNotExist:
            raise forms.ValidationError(f'{email} does not exists')
        return password


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', 'rating')


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'course')
