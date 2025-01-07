from galeria.views import index
from django.urls import path


urlpatterns = [
    path('', index),
]