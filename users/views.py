from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
