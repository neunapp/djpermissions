from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.views.generic import (
    View,
    CreateView
)

# for add permissions
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from django.views.generic.edit import (
    FormView
)

#local apps
from applications.nota.models import Nota

from .forms import (
    UserRegisterForm, 
    LoginForm,
)
#
from .models import User
# 

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        #
        usuario = User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            full_name=form.cleaned_data['full_name'],
            genero=form.cleaned_data['genero'],
            date_birth=form.cleaned_data['date_birth'],
        )
        #recuperar el permiso
        content_type = ContentType.objects.get_for_model(Nota)
        permission = Permission.objects.get(
            codename='view_nota',
            content_type=content_type
        )
        usuario.user_permissions.add(permission)
        # enviar el codigo al email del user
        return super(UserRegisterView, self).form_valid(form)



class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('nota_app:index')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )