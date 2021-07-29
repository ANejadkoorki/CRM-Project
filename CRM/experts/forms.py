from django import forms


class LoginForm(forms.Form):
    """
        represents a form to get users information
    """
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
