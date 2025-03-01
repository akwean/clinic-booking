from django.contrib import admin
from django.urls import include, path
from landing import views as landing_views  # Import landing views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', landing_views.landing_page, name='landing_page'),  # Root URL for landing page
    path('appointments/', include('appointments.urls')),
    path('ai/', include('ai.urls')),
]