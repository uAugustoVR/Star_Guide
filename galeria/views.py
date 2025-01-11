from django.contrib import messages
from galeria.models import photographs
from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Conteúdo exclusivo para clientes Star Guide.")
        messages.error(request, "Faça login ou cadastre-se agora!")
        return redirect('log in')
    else:
        data = photographs.objects.order_by("-date_publication").filter(publication=True)
        return render(request, 'galeria/index.html', {"cards": data})

def imagem(request, photo_id):
    photography = get_object_or_404(photographs, pk=photo_id)
    return render(request, 'galeria/imagem.html', {"photography": photography})

def search(request):
    if not request.user.is_authenticated:
        messages.error(request, "Conteúdo exclusivo para clientes Star Guide.")
        messages.error(request, "Faça login ou cadastre-se agora!")
        return redirect('log in')
    else:
        data = photographs.objects.filter(publication=True)
        if "search" in request.GET:
            name_search = request.GET['search']
            if name_search:
                data = data.filter(name__icontains=name_search)
        return render(request, 'galeria/search.html', {"cards": data})