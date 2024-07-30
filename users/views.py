from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView

# FORMS
from users.forms import SignupForm


class SignupView(FormView):
    #User sign up view
    template_name = 'users/register.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:registerok')

    def form_valid(self, form):
        #save form data
        form.save()
        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    '''Login view'''
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    #Logout view
    template_name = 'users/logout.html'


