from django.urls import path

from Occasion.accounts.views.firm_views import FirmRegisterView, FirmDetailView, EditFirmProfileView, \
    DeleteFirmProfileView
from Occasion.accounts.views.user_views import UserLoginView, UserRegisterView, UserDetailView, EditProfileView, \
    DeleteUserProfileView, UserLogoutView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('register/user/', UserRegisterView.as_view(), name="register user"),
    path('user/<int:pk>/', UserDetailView.as_view(), name='profile details'),
    path('user/edit/<int:pk>/', EditProfileView.as_view(), name='edit user'),
    path('delete/user/<int:pk>/', DeleteUserProfileView.as_view(), name='delete user'),


    path('register/firm/', FirmRegisterView.as_view(), name='register firm'),
    path('firm/<int:pk>/', FirmDetailView.as_view(), name='firm details'),
    path('firm/edit/<int:pk>/', EditFirmProfileView.as_view(), name='edit firm'),
    path('delete/firm/<int:pk>/', DeleteFirmProfileView.as_view(), name='firm delete'),

)