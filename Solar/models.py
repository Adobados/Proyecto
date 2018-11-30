# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from _json import make_encoder

from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.views.i18n import null_javascript_catalog

Us=1

class inventario(models.Model):
    Codigo=models.CharField(max_length=10, primary_key=True,verbose_name='Codigo',null=False,blank=False)
    Producto=models.CharField(max_length=50,verbose_name="Producto")
    Cantidad=models.IntegerField(verbose_name="Cantidad")

    fecha_de_compra=models.DateField(verbose_name="Fecha",null=True)
    Ubicacion=models.CharField(max_length=50,null=True,verbose_name="Ubicacion")

    def __str__(self):
        cadena="Producto {0}"
        return cadena.format(self.Producto)

class Compras(models.Model):
    idVenta=models.CharField(max_length=10, primary_key=True,verbose_name='CodigoVenta',null=False,blank=False)
    Venta=models.ForeignKey('inventario')
    Cantidad=models.IntegerField(verbose_name="Cantidad")
    Precio = models.DecimalField(verbose_name="Precio", decimal_places=2, max_digits=10)
    fecha_de_Venta=models.DateField(verbose_name="FechaVenta",default=timezone.now)
    Ubicacion_de_Venta=models.CharField(max_length=50,null=True,verbose_name="Ubicacion")



    def __str__(self):
        cadena="{0}, Precio:${1} , Dia de venta: {2} "
        return cadena.format(self.Venta,self.Precio,self.fecha_de_Venta)



class Ventas(models.Model):
    Nombre=models.CharField(verbose_name="Nombre",max_length=50)
    Apellidos= models.CharField(verbose_name="Apellido",max_length=50)
    Correo=models.EmailField(verbose_name="Correo")
    Numero_de_Telefono = models.CharField(verbose_name="Numero de Telefono", max_length=50,null=False)
    Fecha=models.DateField(verbose_name="Fecha",default=timezone.now)
    estatus=models.CharField(verbose_name='Status',max_length=50,null=True,default='Pendiente')

    def __str__(self):
        cadena = 'estatus {0} ,Cliente {1} numero :{2}'
        return cadena.format(self.estatus,self.Nombre,self.Numero_de_Telefono)


