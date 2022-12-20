from django.views import generic as views
from django.urls import reverse_lazy
from django.contrib.auth import mixins as auth_mixin

from Occasion.main.forms import EditTruckForm, CreatTruckProfileForm
from Occasion.main.models import Truck


class CreateTruckView(views.CreateView):
    model = Truck
    template_name = 'cars/create_truck_profile.html'
    form_class = CreatTruckProfileForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        try:
            return reverse_lazy('firm details', kwargs={'pk': self.request.user.firmprofile.user_id}, )
        except:
            return reverse_lazy('profile details', kwargs={'pk': self.request.user.id}, )


class TruckDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    form_class = CreatTruckProfileForm
    model = Truck
    template_name = 'cars/truck_profile_details.html'
    context_object_name = 'truck'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user
        return context


class EditTruckView(views.UpdateView):
    model = Truck
    template_name = 'cars/edit_truck_profile.html'
    form_class = EditTruckForm

    def get_success_url(self):
        return reverse_lazy('truck details', kwargs={'pk': self.object.id}, )


class AllTruckView(views.ListView):
    model = Truck
    template_name = 'cars/all_trucks_show.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_truck = context['object_list']
        context.update({'user_truck': user_truck, })
        return context


class DeleteTruckView(views.DeleteView):
    model = Truck
    template_name = 'cars/delete_truck.html'

    def get_success_url(self):
        if not self.request.user.is_staff:
            try:
                return reverse_lazy('firm details', kwargs={'pk': self.request.user.firmprofile.user_id}, )
            except:
                return reverse_lazy('profile details', kwargs={'pk': self.request.user.id}, )
        else:
            return reverse_lazy('all trucks')