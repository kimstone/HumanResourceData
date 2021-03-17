from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from datetime import datetime

from apps.access_control.models import UserAccount


class UserAccountRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Required. Add a valid email address.')

    class Meta:
        model = UserAccount
        fields = ('email', 'username', 'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = UserAccount.objects.exclude(pk=self.instance.pk).get(email=email)
        except UserAccount.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = UserAccount.objects.exclude(pk=self.instance.pk).get(username=username)
        except UserAccount.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)


class UserAccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = UserAccount
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login")


class UserAccountUpdateForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('username', 'email', 'hide_email', 'firstname', 'lastname', 'birthdate', 'hire_date', 'start_date', 'end_date')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = UserAccount.objects.exclude(pk=self.instance.pk).get(email=email)
        except UserAccount.DoesNotExist:
            return email
        raise forms.ValidationError(f'Email {email} is already in use.')

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = UserAccount.objects.exclude(pk=self.instance.pk).get(username=username)
        except UserAccount.DoesNotExist:
            return username
        raise forms.ValidationError(f'Username {username} is already in use.')

    def save(self, commit=True):
        #temp_date = datetime.strptime(self.cleaned_data['birthdate'], "%Y-%m-%d").date()
        account = super(UserAccountUpdateForm, self).save(commit=False)
        account.username =      self.cleaned_data['username']
        account.email =         self.cleaned_data['email'].lower()
        account.hide_email =    self.cleaned_data['hide_email']
        account.firstname =     self.cleaned_data['firstname']
        account.lastname =      self.cleaned_data['lastname']
        account.birthdate =     self.cleaned_data['birthdate']
        account.hire_date =     self.cleaned_data['hire_date']
        account.start_date =    self.cleaned_data['start_date']
        account.end_date =      self.cleaned_data['end_date']
        if commit:
            account.save()
        return account