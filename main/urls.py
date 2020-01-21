from django.urls import path, include
from . import views

from rest_auth.views import LogoutView




urlpatterns = [
    path('login/', views.LoginAPIView.as_view(), name='account_login'),
    path('', include('rest_auth.urls')),
    path('registration/', views.RegisterAPIView.as_view(), name='account_signup'),
    path('registration/', include('rest_auth.registration.urls')),
    path('logout/', LogoutView.as_view(), name='rest_logout'),

    path('weather/', views.WeatherView.as_view(), name="weather"),
]
