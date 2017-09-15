from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    """ The user login form
    """
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)
    user = None

    def clean(self):
        """ Gets the data from the login form 
            and authenticates the user.
        """
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        auth = authenticate(email=email, password=password)
        if not auth:
            raise forms.ValidationError("Wrong Email or Password!")
        else:
            self.user = auth

        return cleaned_data