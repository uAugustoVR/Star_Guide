from galeria.views import index, imagem
from django.urls import path


urlpatterns = [
    path('', index, name= 'index'),
    path('imagem/<int:photo_id>', imagem, name= 'imagem'),
]