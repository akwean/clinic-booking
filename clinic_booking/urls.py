# clinic-booking/clinic_booking/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('landing/', include('landing.urls')),  # Include the landing app's URLs
    path('appointments/', include('appointments.urls')),
]