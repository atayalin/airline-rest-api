"""
URL configuration for airline_rest_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from airline.urls import airline_urls
from aircraft.urls import aircraft_urls

class CustomTokenObtainView(jwt_views.TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if 'access' in response.data:
            token = response.data.pop('access')
            response.data['token'] = token
        if 'refresh' in response.data:
            response.data.pop('refresh')
        return response

urlpatterns = [
    path('api-token-auth/', CustomTokenObtainView.as_view(), name='token'),
    *airline_urls,
    *aircraft_urls,
]
