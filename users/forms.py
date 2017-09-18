from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password, make_password

from .models import User

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


class RegistrationForm(forms.ModelForm):
    """ Contains the fields of the registration form
    """
    confirm_password=forms.CharField()
    class Meta:
        model = User
        fields = ('first_name','last_name','email','password')

    def clean_confirm_password(self):
        """ Checks if the password are matched
        """
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password did not match!"
            )
        return confirm_password

    def clean_email(self):
        """ Checks if the email is already taken
        """
        getclean_email = self.cleaned_data['email']
        emails = User.objects.filter(email=getclean_email)
        if len(emails) != 0:
            raise forms.ValidationError("Sorry but the Email is already TAKEN")
        return getclean_email
        
    def clean(self):
        """ Gets the clean data
        """
        cleaned_data = super(RegistrationForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        return cleaned_data

    def save(self):
        """ Saves the user data
        """
        data = self.cleaned_data
        user = User.objects.create(first_name=data['first_name'], 
                                   last_name=data['last_name'],
                                   email=data['email'],)
        user.set_password(data['password'])
        user.save()
        return user


class UpdateProfileModelForm(forms.ModelForm):
    """ Form for updating the user's profile
    """
    class Meta:
        # what table to use
        model = User
        # what fields to be rendered to template from that table
        fields = ('first_name', 'last_name')


class UpdateEmailModelForm(forms.ModelForm):
    """ Form for updating the user's email
    """
    class Meta:
        # what table to use
        model = User
        # what fields to be rendered to template from that table
        fields = ('email',)

class UpdatePasswordModelForm(forms.Form):
    """ Form for updating the user's password
    """

    oldpassword = forms.CharField(required=True, widget=forms.PasswordInput)
    newpassword = forms.CharField(required=True, widget=forms.PasswordInput)
    retypepassword = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean_oldpassword(self):
        cln_oldpassword = self.cleaned_data.get('oldpassword')
        return cln_oldpassword

    def confirm_password(self):
        # check the new password and confirm password
        new_pass = self.cleaned_data.get('newpassword')
        retype = self.cleaned_data.get('retypepassword')

        if new_pass != retype:
            raise forms.ValidationError("Passwords do not match!")
        return new_pass

    def save(self, *args, **kwargs):
        """save function
        """
        # data from the form
        data = self.cleaned_data
        user = kwargs['user']

        # validate the passwords
        if check_password(data['oldpassword'], user.password):
            # save the new data
            user_update = User.objects.get(id=user.id)
            user_update.password = make_password(data['newpassword'])
            user_update.save()
        else:
            raise forms.ValidationError("Invalid Old Password")
