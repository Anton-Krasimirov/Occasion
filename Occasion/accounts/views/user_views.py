from django.contrib.auth import views as auth_view, get_user_model, login

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.views.generic.base import ContextMixin

from Occasion.accounts.forms import UserCreateForm, FirmProfileCreateForm
from Occasion.accounts.models import UserProfile, FirmProfile


class UserRegisterView(views.CreateView):
    form_class = UserCreateForm
    template_name = 'accounts/create_profile.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):# TODO за да не иска логин след регистрацията
        result = super().form_valid(form)
        # user => self.object
        # request => self.request
        login(self.request, self.object)
        return result


class UserLoginView(auth_view.LoginView, ContextMixin):
    # form_class = UserCreateForm

    template_name = 'accounts/login_user_page.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['checks'] = 'true'

        return context

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()




class UserDetailView(views.DetailView):
    model = UserProfile
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'profile'




class EditProfileView:
    pass





class ChangeUserPasswordView:
    pass
