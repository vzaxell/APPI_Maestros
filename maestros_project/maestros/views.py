from django.shortcuts import render, redirect, get_object_or_404
from .models import Maestro
from .forms import MaestroForm
from django.http import JsonResponse

def index(request):
    query = request.GET.get('q', '')
    if query:
        maestros = Maestro.objects.filter(nombre__icontains=query)
    else:
        maestros = Maestro.objects.all()

    if request.method == "POST":
        form = MaestroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maestros:index')  
    else:
        form = MaestroForm()

    return render(request, 'maestros/index.html', {'form': form, 'maestros': maestros, 'query': query})  

def eliminar_maestro(request, maestro_id):
    maestro = get_object_or_404(Maestro, id=maestro_id)
    maestro.delete()
    return redirect('maestros:index')  

def mapa_view(request):
    lat = request.POST.get('lat', '')
    lon = request.POST.get('lon', '')
    
    context = {
        'lat': lat,
        'lon': lon,
    }
    return render(request, 'maestros/map.html', context)
