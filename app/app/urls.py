"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from frost_met_app.views import MainPage, GetWindDirection, \
    DeleteData, GetData, AllStations, NotFound


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view(template_name="index.html"), name="main_page"),
    path('index/', MainPage.as_view(template_name="index.html"),
         name="main_page"),
    path('delete_data', DeleteData.delete, name='delete_data'),
    path('get_data', GetData.get_data, name='get_data'),
    path('all_stations/', AllStations.as_view(
        template_name="all_stations.html"), name="all_stations"),
    path('get_wind_direction',
         GetWindDirection.get_data, name='get_wind_direction'),
]

handler404 = NotFound.page_not_found_view
