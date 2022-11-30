from django.shortcuts import render
from django.views import generic as views



from Occasion.main.models import CarPhoto, Car


class HomePageView(views.TemplateView):
    template_name = 'index.html'


class DashboardView(views.ListView):
    model = Car
    template_name = 'dashboard.html'
    context_object_name = 'all_cars'


