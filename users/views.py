from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm, RegistrationForm


class UserLogin(TemplateView):
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


class Dashboard(LoginRequiredMixin, TemplateView):
    """ Displays the dashboard page and used LoginRequiredMixin 
        to check the user if logged in.
    """
    template_name = 'dashboard.html'

    def get(self, *args, **kwargs):
        """ Renders the dashboard page
        """
        return render(self.request, self.template_name, {})


class UserLogout(View):
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
            return redirect('user_login')
        return render(self.request, self.template_name, {'form':form})