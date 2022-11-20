
from django.urls import reverse_lazy
from django.views import generic as views


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

