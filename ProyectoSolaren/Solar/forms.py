from django import forms

from .models import inventario,Compras,Ventas

class PostForm(forms.ModelForm):

    class Meta:
        model = inventario
        fields = ('Codigo','Producto','Cantidad','Ubicacion','fecha_de_compra')



class Compra(forms.ModelForm):

    class Meta:
        model = Compras
        fields = ('idVenta','Venta','Cantidad','Precio','fecha_de_Venta','Ubicacion_de_Venta')




class Venta(forms.ModelForm):

    class Meta:
        model = Ventas
        fields = ('Nombre','Apellidos','Correo','Numero_de_Telefono')


