from django import forms


class UserAuthorizationForm(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(max_length=16)


class UserRegistrationForm(forms.Form):
    user_id = forms.IntegerField()
    username = forms.CharField(max_length=80)
    password = forms.CharField(max_length=16)
    email = forms.EmailField()


