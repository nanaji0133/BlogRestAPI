from django.urls import path

from Accounts.views import RegisterView, LoginView, UsersView, LogoutView

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', UsersView.as_view(), name='users'),
    path('register/authtoken/', obtain_auth_token, name='api-auth-token'),
]

