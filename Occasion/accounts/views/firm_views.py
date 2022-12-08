from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login


from Occasion.accounts.forms import FirmProfileCreateForm
from Occasion.accounts.models import FirmProfile
from Occasion.main.models import Car


class FirmRegisterView(views.CreateView):
    form_class = FirmProfileCreateForm
    template_name = 'accounts/firm_profile_create.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result




class FirmDetailView(views.DetailView):
    model = FirmProfile
    template_name = 'accounts/firm_profile_detail.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cars = list(Car.objects.filter(user_id=self.object.user_id))
        context.update({'cars': cars, })

        return context


class EditFirmProfileView(views.UpdateView):
    model = FirmProfile
    template_name = 'accounts/edit_firm_profile.html'
    fields = ('firm_name', 'address', 'phone', 'region', 'email',)

    def get_success_url(self):
        return reverse_lazy('firm details', kwargs={'pk': self.object.pk})


class DeleteFirmProfileView(views.DeleteView):
    model = get_user_model()
    template_name = 'accounts/delete_firm_profile.html'
    success_url = reverse_lazy('index')

