from django import forms
from .models import User


class RegisterFomr(forms.ModelForm):
    password = forms.CharField(label='paassword', widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'gender', 'email']

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다')

        return cd['confirm_password']
