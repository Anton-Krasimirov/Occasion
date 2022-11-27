from django.views import generic as views
from django.urls import reverse_lazy
from django.contrib.auth import mixins as auth_mixin

from Occasion.main.forms import CreatCarProfileForm
from Occasion.main.models import Car


class CreateCarView(views.CreateView):
    model = Car
    template_name = 'cars/create_car_profile.html'
    form_class = CreatCarProfileForm

    def get_success_url(self):
        return reverse_lazy('car details',  kwargs={'pk': self.object.id},)


    def get_form_kwargs(self):# overwrite the function in FormMixin
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user # пренаписваме го и добавяме user , трябва ни в CreatePetForm
        return kwargs


class CarDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    form_class = CreatCarProfileForm
    model = Car
    template_name = 'cars/car_profile_details.html'
    context_object_name = 'car'

    def get_queryset(self):
        return Car.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['car'] = Car.objects.filter(pk=self.kwargs.get('pk'))



class EditCarView(views.UpdateView):
    pass
# TODO form_class and template_name


class DeleteCarView(views.DeleteView):
    pass
# TODO form_class and template_name
