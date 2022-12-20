from django.views import generic as views
from django.urls import reverse_lazy
from django.contrib.auth import mixins as auth_mixin

from Occasion.main.forms import CreatMotorProfileForm, EditMotorForm
from Occasion.main.models import Motorbike


class CreateMotorView(views.CreateView):
    model = Motorbike
    template_name = 'cars/create_motor_profile.html'
    form_class = CreatMotorProfileForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        try:
            return reverse_lazy('firm details', kwargs={'pk': self.request.user.firmprofile.user_id}, )
        except:
            return reverse_lazy('profile details', kwargs={'pk': self.request.user.id}, )


class MotorDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    form_class = CreatMotorProfileForm
    model = Motorbike
    template_name = 'cars/motor_profile_details.html'
    context_object_name = 'motor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user
        return context


class EditMotorView(views.UpdateView):
    model = Motorbike
    template_name = 'cars/edit_motor_profile.html'
    form_class = EditMotorForm

    def get_success_url(self):
        return reverse_lazy('motor details', kwargs={'pk': self.object.id}, )


class AllMotorsView(views.ListView):
    model = Motorbike
    template_name = 'cars/all_motors_show.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_motors = context['object_list']
        context.update({'user_motors': user_motors, })
        return context


class DeleteMotorView(views.DeleteView):
    model = Motorbike
    template_name = 'cars/delete_motor.html'

    def get_success_url(self):
        if not self.request.user.is_staff:
            try:
                return reverse_lazy('firm details', kwargs={'pk': self.request.user.firmprofile.user_id}, )
            except:
                return reverse_lazy('profile details', kwargs={'pk': self.request.user.id}, )
        else:
            return reverse_lazy('all motors')