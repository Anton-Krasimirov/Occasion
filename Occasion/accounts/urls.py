from django.urls import path

from Occasion.accounts.views import UserLoginView, UserRegisterView, FirmRegisterView, UserDetailView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('register/', UserRegisterView.as_view(), name="register user"),
    path('register/firm/', FirmRegisterView.as_view(), name='register firm'),
    path('<int:pk>/', UserDetailView.as_view(), name='profile details'),
)