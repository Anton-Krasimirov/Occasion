from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
from Occasion.accounts.forms import FirmProfileCreateForm
from Occasion.accounts.models import FirmProfile


class FirmRegisterView(views.CreateView):
    form_class = FirmProfileCreateForm
    template_name = 'accounts/firm_profile_create.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class FirmDetailView(views.DetailView):
    model = FirmProfile
    template_name = 'accounts/firm_profile_detail.html'
    context_object_name = 'profile'


class EditFirmProfileView(views.UpdateView):
    model = FirmProfile
    template_name = 'accounts/edit_firm_profile.html'
    fields = ('firm_name', 'address', 'phone', 'region', 'email',)

    def get_success_url(self):
        return reverse_lazy('firm details', kwargs={'pk': self.object.pk})


class DeleteFirmProfileView(views.DeleteView):
    model = FirmProfile
    template_name = 'accounts/delete_firm_profile.html'
    success_url = reverse_lazy('index')


class ChangeFirmProfileView(auth_views.PasswordChangeView):
    pass
