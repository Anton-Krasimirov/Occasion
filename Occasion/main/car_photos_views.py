from django.contrib.auth import mixins as auth_mixin
from django.urls import reverse_lazy

from django.views import generic as views


from Occasion.main.forms import CreatCarPhotoForm
from Occasion.main.models import CarPhoto


class CreateCarPhotoView(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = CarPhoto
    template_name = 'cars/photo_create.html'
    form_class = CreatCarPhotoForm

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['car'] = self.request.user....
    #     return kwargs

    def get_success_url(self):
        try:
            return reverse_lazy('firm details', kwargs={'pk': self.request.user.firmprofile.user_id}, )
        except:
            return reverse_lazy('profile details', kwargs={'pk': self.request.user.id}, )

class DeleteCarPhotoView(views.DeleteView):
    model = CarPhoto
    template_name = 'cars/delete_photo.html'

    def get_success_url(self):
        try:
            return reverse_lazy('firm details', kwargs={'pk': self.request.user.firmprofile.user_id}, )
        except:
            return reverse_lazy('profile details', kwargs={'pk': self.request.user.id}, )
