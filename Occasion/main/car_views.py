from django.views import generic as views
from django.urls import reverse_lazy
from django.contrib.auth import mixins as auth_mixin

from Occasion.main.forms import CreatCarProfileForm, EditCarForm
from Occasion.main.models import Car


class CreateCarView(views.CreateView):
    model = Car
    template_name = 'cars/create_car_profile.html'
    form_class = CreatCarProfileForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        try:
            return reverse_lazy('firm details', kwargs={'pk': self.request.user.firmprofile.user_id}, )
        except:
            return reverse_lazy('profile details', kwargs={'pk': self.request.user.id}, )


class CarDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    form_class = CreatCarProfileForm
    model = Car
    template_name = 'cars/car_profile_details.html'
    context_object_name = 'car'

    # def get_queryset(self):
    #     return Car.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user
        return context


class EditCarView(views.UpdateView):
    model = Car
    template_name = 'cars/edit_car_profile.html'
    form_class = EditCarForm

    def get_success_url(self):
        return reverse_lazy('car details', kwargs={'pk': self.object.id}, )


class AllCarsView(views.ListView):
    model = Car
    template_name = 'cars/all_cars_show.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_cars = context['object_list']
        context.update({'user_cars': user_cars, })
        return context


class DeleteCarView(views.DeleteView):
    model = Car
    template_name = 'cars/delete_car.html'

    def get_success_url(self):
        try:
            return reverse_lazy('firm details', kwargs={'pk': self.request.user.firmprofile.user_id}, )
        except:
            return reverse_lazy('profile details', kwargs={'pk': self.request.user.id}, )