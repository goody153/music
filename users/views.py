from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm, RegistrationForm

from .forms import LoginForm, UpdateProfileModelForm
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

#====================================================================
#====================================================================
#====================================================================

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
        """render a user's profile
        """
        # get the user that is currently logged in
        user = get_object_or_404(User, id=self.request.user.id)
        return render(self.request, self.template_name, {'user':user})


class UpdateProfileView(TemplateView):
    """ Update the user's first and last names
    """
    template_name = 'user/edit.html'

    def get(self, *args, **kwargs):
        #import pdb;pdb.set_trace()
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
