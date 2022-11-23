from django.views import generic as views
from django.urls import reverse_lazy


class CreateCarView(views.CreateView):
    template_name = 'cars/create_car_profile.html'
    # form_class = CreateCarForm # TODO form
    success_url = reverse_lazy('profile details')

class EditCarView(views.UpdateView):
    pass
# TODO form_class and template_name


class DeleteCarView(views.DeleteView):
    pass
# TODO form_class and template_name
