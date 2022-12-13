

from django.urls import path


from Occasion.main.car_views import CreateCarView, CarDetailsView, AllCarsView, EditCarView, DeleteCarView
from Occasion.main.home_views import HomePageView, DashboardView
from Occasion.main.truck_views import CreateTruckView, TruckDetailsView, EditTruckView, AllTruckView, DeleteTruckView

urlpatterns = (
    path('', HomePageView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('create/car/', CreateCarView.as_view(), name='create car'),
    path('edit/car/<int:pk>/', EditCarView.as_view(), name='edit car'),
    path('car/details/<int:pk>/', CarDetailsView.as_view(), name='car details'),
    path('car/all_cars/', AllCarsView.as_view(), name='all cars'),
    path('car/delete/<int:pk>/', DeleteCarView.as_view(), name='delete car'),

    path('create/truck/', CreateTruckView.as_view(), name='create truck'),
    path('truck/details/<int:pk>/', TruckDetailsView.as_view(), name='truck details'),
    path('edit/truck/<int:pk>/', EditTruckView.as_view(), name='edit truck'),
    path('truck/all_trucks/', AllTruckView.as_view(), name='all trucks'),
    path('truck/delete/<int:pk>/', DeleteTruckView.as_view(), name='delete truck'),
)