from django.contrib.auth import views as auth_view, get_user_model, login

from django.urls import reverse_lazy
from django.views import generic as views
from django.views.generic.base import ContextMixin

from Occasion.accounts.forms import UserCreateForm
from Occasion.accounts.models import UserProfile


class UserRegisterView(views.CreateView):
    form_class = UserCreateForm
    template_name = 'accounts/create_profile.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):  # TODO за да не иска логин след регистрацията
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


class EditProfileView(views.UpdateView):
    model = UserProfile
    template_name = 'accounts/edit_profile.html'
    fields = ('first_name', 'last_name', 'email', 'phone', 'region')

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})


class DeleteUserProfileView(views.DeleteView):
    # form_class = UserDeleteForm
    model = get_user_model()
    template_name = 'accounts/delete_user.html'
    success_url = reverse_lazy('index')


class ChangeUserPasswordView(auth_view.PasswordChangeView):
    pass
