from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import generic as views


class HomePageView(views.TemplateView):
    template_name = 'index.html'


class DashboardView(views.ListView):
    model = get_user_model()
    template_name = 'dashboard.html'



