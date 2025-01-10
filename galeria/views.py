from django.shortcuts import render, get_object_or_404
from galeria.models import photographs

def index(request):
    data = photographs.objects.order_by("-date_publication").filter(publication=True)
    return render(request, 'galeria/index.html', {"cards": data})

def imagem(request, photo_id):
    photography = get_object_or_404(photographs, pk=photo_id)
    return render(request, 'galeria/imagem.html', {"photography": photography})

def search(request):
    data = photographs.objects.filter(publication=True)
    if "search" in request.GET:
        name_search = request.GET['search']
        if name_search:
            data = data.filter(name__icontains=name_search)
    return render(request, 'galeria/search.html', {"cards": data})