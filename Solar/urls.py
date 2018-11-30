

from django.conf.urls import url
from Solar.views import post_detail,Datos,post_list,BuscaProducto,Compras,Inventario,Formulario,Ventas




urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'^Productos', post_detail, name='post_detail'),
    url(r'^BuscaProducto', BuscaProducto, name='BuscaProducto'),
    url(r'^Datos', Datos, name='Datos'),
    # url(r'^Compras', Compras, name='Compras'),
    url(r'^Compras', Compras, name='Compras'),
    url(r'^Inicio', post_list, name='post_list'),
    url(r'^Inventario', Inventario, name='Inventario'),
    url(r'^Formulario', Formulario, name='Formulario'),
    url(r'^Ventas', Ventas, name='Ventas'),


]
