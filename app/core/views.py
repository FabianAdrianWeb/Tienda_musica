from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def productos(request):
    return render(request, 'paginas/productos.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')