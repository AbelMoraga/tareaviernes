from django.urls import path
from . import views

# aca si se agregan todas las ulr de la app
urlpatterns = [
    path('', views.index),
    path('vista/',views.s2),
]