from django.urls import path
from apps.galeria.views import \
    index, imagem, search, post, delete, update


urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:photo_id>', imagem, name='imagem'),
    path('search', search, name='search'),
    path('post', post, name='post'),
    path('delete/<int:photo_id>', delete, name='delete'),
    path('update/<int:photo_id>', update, name='update'),
]