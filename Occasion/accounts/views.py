from django.contrib.auth import views as auth_view
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from Occasion.accounts.forms import UserCreateForm, FirmProfileCreateForm
from Occasion.accounts.models import UserProfile


class UserRegisterView(views.CreateView):
    form_class = UserCreateForm
    template_name = 'accounts/create_profile.html'
    success_url = reverse_lazy('dashboard')

class UserLoginView(auth_view.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):# TODO zakomentiram go i raboti correct !!!
        if self.success_url:
            return self.success_url
        return super().get_success_url()

class FirmRegisterView(views.CreateView):
    form_class = FirmProfileCreateForm
    template_name = 'accounts/firm_profile_create.html'
    success_url = reverse_lazy('dashboard')


class UserDetailView(views.DetailView):
    model = UserProfile
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'profile'


class EditProfileView:
    pass


class ChangeUserPasswordView:
    pass
