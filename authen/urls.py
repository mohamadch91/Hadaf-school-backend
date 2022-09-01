from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sregister/', StudentRegisterView.as_view(), name='auth_register'),
    path('tregister/', TeacherRegisterView.as_view(), name='auth_register'),
    path('uregister/',UserRegisterView.as_view(),name="user register"),
    path('users/', UserListView.as_view(), name='user_list'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
    path('sms/login/',OTPViewLogin.as_view(),name="OTP view login"),
    path('sms/register',OTPViewRegister.as_view(),name="OTP viewvregister "),
    path('delete/',deleteUser.as_view(),name="delete user"),
    path('change_password/', changePasswordViews.as_view(), name='auth_change_password'),
    path('admin_login/', adminLoginbyUserView.as_view(), name='admin_login'),



]