from django.contrib.auth import mixins as auth_mixin
from django.views import generic as views

from Occasion.main.models import CarPhoto


class CreateCarPhotoView(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = CarPhoto
    template_name = 'cars/photo_create.html'
    context_object_name = 'car_photos'
