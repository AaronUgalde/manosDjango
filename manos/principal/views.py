from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context

# Create your views here.
def home(request):
    print("hola")
    doc_externo=open("principal\plantillas\index.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)

def funcion(request):
    print("doajkñ{asjd")
    return True