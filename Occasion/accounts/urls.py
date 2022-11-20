from django.urls import path

from Occasion.accounts.views.firm_views import FirmRegisterView, FirmDetailView
from Occasion.accounts.views.user_views import UserLoginView, UserRegisterView, UserDetailView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('register/user/', UserRegisterView.as_view(), name="register user"),
    path('register/firm/', FirmRegisterView.as_view(), name='register firm'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='profile details'),
    path('firm/<int:pk>/', FirmDetailView.as_view(), name='firm details'),

)