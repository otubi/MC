from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # You can define more URL patterns for other views here
]
