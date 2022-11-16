from django.urls import path

from Occasion.accounts.views import UserLoginView, UserRegisterView, FirmRegisterView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('register/', UserRegisterView.as_view(), name="register user"),
    path('register/firm/', FirmRegisterView.as_view(), name='register firm'),
)