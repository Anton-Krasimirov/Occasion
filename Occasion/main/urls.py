

from django.urls import path

from Occasion.main.car_photos_views import CreateCarPhotoView
from Occasion.main.car_views import CreateCarView, CarDetailsView, AllCarsView
from Occasion.main.home_views import HomePageView, DashboardView

urlpatterns = (
    path('', HomePageView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('create/car/', CreateCarView.as_view(), name='create car'),
    path('car/details/<int:pk>/', CarDetailsView.as_view(), name='car details'),
    path('car/all_cars/', AllCarsView.as_view(), name='all cars'),

    path('car/photo/create/', CreateCarPhotoView.as_view(), name='photo create'),
)