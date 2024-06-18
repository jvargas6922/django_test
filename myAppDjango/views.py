from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola mundo desde Django!")

def despedida(requets):
    return HttpResponse("Hasta luego mundo desde Django!")

def mensaje(request,mensaje):
    mensaje ={mensaje:mensaje}
    return HttpResponse(mensaje)

def simple(request):
    return render(request, 'simple.html')

def dinamico(request,mensaje):
    tecnologias = ['HTML5','CSS3','JavaScript','Bootstrap','Python','posgresql','Django']
    context ={ 'mensaje': mensaje, 'tecnologias':tecnologias}
    return render(request, 'dinamico_2.html',context)
    
