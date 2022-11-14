from django.urls import path

from Occasion.accounts.views import UserLoginView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
)