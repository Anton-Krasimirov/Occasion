from django.shortcuts import render
from django.views import generic as views

from Occasion.accounts.models import OccasionUser


class HomePageView(views.TemplateView):
    template_name = 'index.html'


class DashboardView(views.ListView):
    model = OccasionUser# TODO delete import OccasionUser
    #TODO model =  da pokazwa wsichki koli
    template_name = 'dashboard.html'
    # TODO context_object_name =
