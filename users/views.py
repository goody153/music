from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm, RegistrationForm

from .forms import LoginForm, UpdateProfileModelForm, UpdateEmailModelForm, UpdatePasswordModelForm
from .models import User

class UserLoginView(TemplateView):
    """ User login account
    """
    template_name = 'auth/login.html'

    def get(self, *args, **kwargs):
        """ Renders the login form
        """
        form = LoginForm()
        return render(self.request, self.template_name, {'form':form})

    def post(self, *args, **kwargs):
        """ submits the data
        """
        form = LoginForm(self.request.POST)
        if form.is_valid():
            login(self.request, form.user)
            return redirect('dashboard')

        return render(self.request, self.template_name, {'form':form})


class DashboardView(LoginRequiredMixin, TemplateView):
    """ Displays the dashboard page and used LoginRequiredMixin 
        to check the user if logged in.
    """
    template_name = 'dashboard.html'

    def get(self, *args, **kwargs):
        """ Renders the dashboard page
        """
        return render(self.request, self.template_name, {})


class UserLogoutView(View):
    """ Logout the user account
    """
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('user_login')


class RegisterView(TemplateView):
    """ Registers the new user
    """
    template_name = 'registration.html'

    def get(self, *args, **kwargs):
        """ Renders the registration form
        """
        form = RegistrationForm()
        return render(self.request, self.template_name, {'form':form})

    def post(self, *args, **kwargs):
        """ Gets the data
        """
        form = RegistrationForm(self.request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(self.request, email=self.request.POST['email'], 
                                              password=self.request.POST['password'])
            login(self.request, user)
            return redirect('dashboard')
        return render(self.request, self.template_name, {'form':form})


class UserProfileView(View):
    """ display a user's profile
    """
    template_name = 'user/profile.html'

    def get(self, *args, **kwargs):
        """ render a user's profile
        """
        # get the user that is currently logged in
        return render(self.request, self.template_name, {'user':self.request.user})


class UpdateProfileView(TemplateView):
    """ Update the user's first and last names
    """
    template_name = 'user/edit.html'

    def get(self, *args, **kwargs):
        """ display
        """
        user = get_object_or_404(User, id=self.request.user.id)
        form = UpdateProfileModelForm(instance=user)
        return render(self.request, self.template_name, {'form':form})

    def post(self, *args, **kwargs):
        """update the user's profile (first name, last name)
        """
        user = get_object_or_404(User, id=self.request.user.id)
        form = UpdateProfileModelForm(self.request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
        return render(self.request, self.template_name, {'form':form})



class UpdateEmailView(TemplateView):
    """ Updates the user's email
    """
    template_name = 'user/editemail.html'

    def get(self, *args, **kwargs):
        """display form
        """
        user = get_object_or_404(User, id=self.request.user.id)
        form = UpdateEmailModelForm(instance=user)
        return render(self.request, self.template_name, {'form':form,
                                                         'user':user
                                                        })

    def post(self, *args, **kwargs):
        """save the changes of email
        """
        user = get_object_or_404(User, id=self.request.user.id)
        form = UpdateEmailModelForm(self.request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
        return render(self.request, self.template_name, {'form':form,
                                                         'user':user
                                                        })



class UpdatePasswordView(TemplateView):
    """ Updates the user's password
    """
    template_name = 'user/editpassword.html'

    def get(self, *args, **kwargs):
        """display the form
        """
        form = UpdatePasswordModelForm()
        return render(self.request, self.template_name, {'form':form,
                                                        'user':self.request.user
                                                        })

    def post(self, *args, **kwargs):
        """save the changes
        """
        form = UpdatePasswordModelForm(self.request.POST)
        if form.is_valid():
            # save the form and relogin the user, using the new credentials
            form.save(user=self.request.user)
            user = authenticate(self.request, email = self.request.user.email,
                                            password = self.request.POST['new_password'])
            login(self.request, user)
            return redirect('user_profile')
        return render(self.request, self.template_name, {'form':form,
                                                        'user':self.request.user
                                                        })
