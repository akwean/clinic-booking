# clinic-booking/appointments/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('success/', views.appointment_success, name='appointment_success'),
    path('history/', views.appointment_history, name='appointment_history'),
]