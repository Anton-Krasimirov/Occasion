

from django.urls import path

from Occasion.main.views import HomePageView

urlpatterns = (
    path('', HomePageView.as_view(), name='index'),

)