# Licença: CC BY-NC 4.0
# Este código pode ser usado, modificado e redistribuído **apenas para fins não comerciais**.
# Mais detalhes: https://creativecommons.org/licenses/by-nc/4.0/

import os 
from django.conf import settings
from django.contrib import messages
from apps.galeria.models import photographs
from apps.galeria.forms import PhotographyForms
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
    return render(request, 'galeria/image.html', {"photography": photography})

def search(request):
    if not request.user.is_authenticated:
        messages.error(request, "Conteúdo exclusivo para clientes Star Guide.")
        messages.error(request, "Faça login ou cadastre-se agora!")
        return redirect('log in')
    
    data = photographs.objects.order_by('-date_publication').filter(publication=True)
    if "search" in request.GET:
        name_search = request.GET['search']
        if name_search:
            data = data.filter(name__icontains=name_search)
    return render(request, 'galeria/index.html', {"cards": data})
    
def post(request):
    if not request.user.is_authenticated:
        messages.error(request, "Ferramenta exclusiva para clientes Star Guide.")
        messages.error(request, "Faça login ou cadastre-se agora!")
        return redirect('log in')
    else:
        form = PhotographyForms
    
        if request.method == 'POST':
            form = PhotographyForms(request.POST, request.FILES)
            if form.is_valid():
                photo = form.save(commit=False)
                photo.user = request.user
                photo.save()
                messages.success(request, "Foto publicada com sucesso!")
                return redirect('index')
        return render(request, "galeria/post.html", {'form': form})

def update(request, photo_id):
    photo = photographs.objects.get(id=photo_id)
    form = PhotographyForms(instance=photo)

    if request.user != photo.user:
        messages.error(request, "Você não tem permissão para editar esta foto.")
        return redirect('index')

    if request.method == 'POST':
        form = PhotographyForms(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            messages.success(request, "Foto editada com sucesso!")
            return redirect('index')
        else:
            messages.error(request, "Erro ao editar a foto tente novamente mais tarde!")
        
    return render(request, "galeria/update.html", {'form': form, 'photo_id': photo_id})

def delete(request, photo_id):
    photo = get_object_or_404(photographs, id=photo_id)

    if request.user != photo.user:
        messages.error(request, "Você não tem permissão para excluir esta foto.")
        return redirect('index')

    if request.method == "POST":
        file_path = photo.photo.path
        if os.path.exists(file_path):
            os.remove(file_path)
        photo.delete()
        messages.success(request, "Foto excluída com sucesso!")
        return redirect('index')
    
    return render(request, "galeria/delete.html", {"photo": photo})

def filter(request, category):
    data = photographs.objects.order_by("-date_publication").filter(publication=True, category=category)
    return render(request, 'galeria/index.html', {"cards": data})