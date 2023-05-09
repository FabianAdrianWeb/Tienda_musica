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