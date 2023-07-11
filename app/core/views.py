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
    # Renderiza la plantilla 'index.html'
    return render(request, 'index.html')

def productos(request):
    # Obtiene todos los productos de la base de datos
    productos = Producto.objects.all()
    # Crea un contexto con la lista de productos
    contexto = {'productos': productos}
    # Renderiza la plantilla 'productos.html' con el contexto
    return render(request, 'paginas/productos.html', contexto)

def contacto(request):
    # Renderiza la plantilla 'contacto.html'
    return render(request, 'paginas/contacto.html')

def api(request):
    # Realiza una solicitud GET a una API externa (iTunes)
    response = requests.get('https://itunes.apple.com/us/rss/topsongs/limit=10/json')
    # Convierte la respuesta a formato JSON
    data = response.json()
    songs_data = []
    # Itera sobre las canciones obtenidas de la respuesta
    for song in data['feed']['entry']:
        # Extrae los datos relevantes de cada canción
        song_data = {
            'name': song['im:name']['label'],
            'artist': song['im:artist']['label'],
            'image': song['im:image'][-1]['label']
        }
        # Agrega los datos de la canción a la lista
        songs_data.append(song_data)
    context = {'songs': songs_data}
    # Renderiza la plantilla 'api.html' con el contexto de canciones
    return render(request, 'paginas/api.html', context)

def login(request):
    # Renderiza la plantilla 'login.html'
    return render(request, 'paginas/login.html')

def registro(request):
    # Si el usuario ya está autenticado, redirige a 'index'
    if request.user.is_authenticated:
        return redirect('index')
    # Si el método de la solicitud es POST, procesa el formulario de registro
    if request.method == 'POST':
        form = UsuarioRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'El usuario "{username}" se creó exitosamente')
    else:
        form = UsuarioRegisterForm()
    context = {'form' : form}
    # Renderiza la plantilla 'registro.html' con el formulario de registro
    return render(request, 'paginas/registro.html', context)

@csrf_exempt
def administrar_productos(request, action, id):
    # Si el usuario no está autenticado o no es un miembro del personal, redirige a 'index'
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect(index)

    data = {"mesg": "", "form": ProductoForm, "action": action, "id": id}

    if action == 'ins':
        # Si la acción es 'ins' (insertar), verifica si se envió un formulario POST
        if request.method == "POST":
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El producto fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos vehículos con el mismo ID!"

    elif action == 'upd':
        # Si la acción es 'upd' (actualizar), obtiene el objeto Producto correspondiente al ID proporcionado
        objeto = Producto.objects.get(id=id)
        if request.method == "POST":
            form = ProductoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El producto fue actualizado correctamente!"
        data["form"] = ProductoForm(instance=objeto)

    elif action == 'del':
        # Si la acción es 'del' (eliminar), intenta eliminar el producto correspondiente al ID proporcionado
        try:
            Producto.objects.get(id=id).delete()
            data["mesg"] = "¡El producto fue eliminado correctamente!"
            return redirect(administrar_productos, action='ins', id='-1')
        except:
            data["mesg"] = "¡El producto ya estaba eliminado!"

    # Obtiene todos los productos de la base de datos ordenados por ID
    data["list"] = Producto.objects.all().order_by('id')
    # Renderiza la plantilla 'administrar_productos.html' con los datos necesarios
    return render(request, "paginas/administrar_productos.html", data)
