from django.contrib.auth import views
from django.shortcuts import render
from django.urls import reverse_lazy


class UserRegisterView:
    pass


class UserLoginView(views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):# TODO probvai da go zakomentiram i da widq kyde shte me preprati
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserDetailView:
    pass


class EditProfileView:
    pass


class ChangeUserPasswordView:
    pass
