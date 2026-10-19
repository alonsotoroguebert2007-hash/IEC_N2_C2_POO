from Datos.repositorios.repositorio_tienda import listado_tienda, guardar_tienda, tienda_por_nombre
from prettytable import PrettyTable
from Datos.modelos.tienda import Tienda


def cargar_tienda(tabla: PrettyTable):
    tiendas = listado_tienda()
    tabla.field_names = ['id', 'nombre', 'correo', 'telefono']

    if tiendas:
        for tienda in tiendas:
            tabla.add_row([tienda.id_tienda, tienda.nombre, tienda.correo, tienda.telefono])

    return tabla  

def buscar_tienda(tabla: PrettyTable,nombre):
    tiendas = tienda_por_nombre(nombre)
    tabla.field_names = ['id', 'nombre', 'correo', 'telefono']

    if tiendas:
            for tienda in tiendas:
                tabla.add_row([tienda.id_tienda, tienda.nombre, tienda.correo, tienda.telefono])
    
    return tabla  

def crear_tienda(estado, nombre):
     nueva_tienda = Tienda()
     nueva_tienda.estado = estado
     nueva_tienda.nombre = nombre
     tienda = guardar_tienda(nueva_tienda)
     if tienda == 1:
          print(f'Se ha guardado la tienda {nueva_tienda.nombre} con ID {nueva_tienda.id_tienda}')
                                                              