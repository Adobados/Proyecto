# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.context_processors import csrf
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView

from httplib import HTTP

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from distutils.command.register import register

from  Solar.forms import *
from django.template import RequestContext

from django.shortcuts import render, redirect, render_to_response,  get_object_or_404
from .models import inventario
from .forms import PostForm,Compra,Venta


# Create your views here.



def post_list(request):
    return render(request, 'Solar/Index.html', {})

def Ventas(request):
    if request.method == "POST":
        form = Compra(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('Ventas')
    else:
        form = Compra
        return render(request, 'Solar/FormularioVentas.html', {'form': form})


def post_detail(request):
    if request.method == "POST":
        form = Compra(request.POST)
        if form.is_valid():

            return redirect('Productos')
    else:

        return render(request, 'Solar/Productos.html', {})

def Inventario(request):
    return render(request, 'Solar/Inventario.html', {})

def Datos(request):
    return render(request, 'Solar/muestra_datos.html', {'inventario': inventario.objects.all()})

def Formulario(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()

            post.save()
            return redirect('Formulario')
    else:
        form = PostForm()
        return render(request, 'Solar/Formulario.html', {'form': form})


def Compras(request):


    return render(request, 'Solar/FormularioCompras.html', {})


from Solar.tables import SimpleTable


def BuscaProducto(request):
    if request.method == 'POST' and 'Codigo' in request.POST:
        if inventario.objects.filter(Codigo=request.POST['Codigo']).count()>0:
            producto =inventario.objects.filter(Codigo=request.POST['Codigo'])
            table_class = SimpleTable(producto)

            contexto = {
                'datos': producto,
                'tabla':table_class
            }

            return render(request,'Solar/Existencias.html',contexto)
        else: return HttpResponse("No existe Producto")
    else:
        return HttpResponse("No hay datos.")




def Administrador(request):
    return render(request, 'Solar/InicioAdmin.html', {})



class VentasListView(ListView):
    model=Ventas
    context_object_name='ventas'

class VentasCreateView(CreateView):
    model=Ventas
    fields=('idVenta','Venta','Cantidad')
    success_url = reverse_lazy('ventas_changelist')

class VentasUpdateView(UpdateView):
    model = Ventas
    fields = ('idVenta', 'Venta', 'Cantidad')
    success_url = reverse_lazy('ventas_changelist')

def Compras(request):
    if request.method == "POST":
        form = Venta(request.POST)
        if form.is_valid():

            post = form.save()
            post.save()
            return HttpResponse("Uno de nustros socios se contactara con usted en unos momentos...")

    else:
        form = Venta
        return render(request, 'Solar/FormularioCompras.html', {'form': form})
