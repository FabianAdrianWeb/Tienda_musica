from django.shortcuts import render
from .forms import *
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
import requests
from django.views import View
from .forms import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request, 'index.html')

def productos(request):
    productos = Producto.objects.all()
    contexto = {'productos': productos}
    return render(request, 'paginas/productos.html', contexto)


def contacto(request):
    return render(request, 'paginas/contacto.html')

def api(request):
    response = requests.get('https://itunes.apple.com/us/rss/topsongs/limit=10/json')
    data = response.json()
    songs_data = []
    for song in data['feed']['entry']:
        song_data = {
            'name': song['im:name']['label'],
            'artist': song['im:artist']['label'],
            'image': song['im:image'][-1]['label']
        }
        songs_data.append(song_data)
    context = {'songs': songs_data}
    return render(request, 'paginas/api.html', context)



def login(request):
    return render(request, 'paginas/login.html')

def registro(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = UsuarioRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'El usuario "{username}" se creo exitosamente')
    else:
        form = UsuarioRegisterForm()
    context = {'form' : form}
    return render(request, 'paginas/registro.html',context)

@csrf_exempt
def administrar_productos(request, action, id):
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect(index)

    data = {"mesg": "", "form": ProductoForm, "action": action, "id": id}

    if action == 'ins':
        if request.method == "POST":
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El producto fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos vehículos con el mismo ID!"

    elif action == 'upd':
        objeto = Producto.objects.get(id=id)
        if request.method == "POST":
            form = ProductoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El producto fue actualizado correctamente!"
        data["form"] = ProductoForm(instance=objeto)

    elif action == 'del':
        try:
            Producto.objects.get(id=id).delete()
            data["mesg"] = "¡El producto fue eliminado correctamente!"
            return redirect(administrar_productos, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El producto ya estaba eliminado!"

    data["list"] = Producto.objects.all().order_by('id')
    return render(request, "paginas/administrar_productos.html", data)