from django.shortcuts import render
from .forms import *
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
import requests
from django.views import View
from google.oauth2 import service_account
from googleapiclient.discovery import build
# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def productos(request):
    return render(request, 'paginas/productos.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')



def api(request):
    # Autenticación con tu clave de API
    SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
    SERVICE_ACCOUNT_FILE = 'ruta/a/tu/archivo.json'
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # Crea el objeto de servicio de la API de YouTube Music
    youtube_music = build('youtubemusic', 'v1', credentials=credentials)

    # Obtén las canciones más escuchadas
    chart_response = youtube_music.chart().list(chart='mostPopular', regionCode='US').execute()
    songs = chart_response['songs']

    # Renderiza los resultados en una plantilla de Django
    return render(request, 'paginas/api.html', {'songs': songs})


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