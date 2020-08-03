from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='alerts-home'),
    path('honk/', views.honk, name='alerts-honk'),
    path('settings/', views.settings, name='alerts-settings')
]
