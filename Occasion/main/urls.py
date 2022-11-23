

from django.urls import path

from Occasion.main.car_views import CreateCarView
from Occasion.main.home_views import HomePageView, DashboardView

urlpatterns = (
    path('', HomePageView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('create/car/', CreateCarView.as_view(), name='create car'),
)