from django.contrib import admin
from django.urls import path, include
from data import views  # Correct the import for the 'views' module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('data.urls')),
    path('', views.home, name='home'),
]
