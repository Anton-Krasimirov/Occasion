from django.shortcuts import render
from django.views import generic as views

from Occasion.accounts.models import OccasionUser
from Occasion.main.models import CarPhoto


class HomePageView(views.TemplateView):
    template_name = 'index.html'


class DashboardView(views.ListView):
    model = CarPhoto# TODO delete import OccasionUser
    #TODO model =  da pokazwa wsichki koli
    template_name = 'dashboard.html'
    context_object_name = 'car_photos'
