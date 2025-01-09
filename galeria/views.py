from django.shortcuts import render, get_object_or_404
from galeria.models import photographs

def index(request):
    data = photographs.objects.all()

    return render(request, 'galeria/index.html', {"cards": data})

def imagem(request, photo_id):
    photography = get_object_or_404(photographs, pk=photo_id)
    return render(request, 'galeria/imagem.html', {"photography": photography})