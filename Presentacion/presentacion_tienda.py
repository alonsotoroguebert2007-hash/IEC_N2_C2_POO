from Negocio.negocio_tienda import cargar_tienda, crear_tienda, buscar_tienda
from Datos.repositorios.repositorio_tienda import tienda_por_id, guardar_tienda
from Datos.modelos.tienda import Tienda
from prettytable import PrettyTable

def mostrar_tienda():
    tabla_tienda = PrettyTable()
    tabla_tienda = cargar_tienda(tabla_tienda)
    print(tabla_tienda)

def datos_tienda():
    estado = input('Ingrese el estado de la tienda: ')
    nombre = input('Ingrese el nombre de la tienda: ')
    crear_tienda(estado,nombre.title())

def buscar_nombre_tienda(nombre):
    tabla_tienda = PrettyTable()
    tabla_tienda = buscar_tienda(tabla_tienda,nombre)
    print(tabla_tienda)

def actualizar_tienda():
    nombre = input('Ingrese el nombre de la tienda: ')
    buscar_nombre_tienda(nombre)
    id_ingresado = input('Ingrese ID de tienda para modificar: ')
    tienda = tienda_por_id(id_ingresado)
    nombre_nuevo = input('Ingrese nombre nuevo de tienda (o ENTER para conservar): ')
    estado_nuevo = input('Ingrese estado nuevo de tienda (o ENTER para conservar): ')

    if nombre_nuevo != '':
        tienda.nombre_tienda = nombre_nuevo.title()
    if estado_nuevo != '':
        tienda.estado = estado_nuevo.title()
    respuesta = guardar_tienda(tienda)
    if respuesta == 1:
        print(f'Tienda {tienda.nombre_tienda} actualizada con exito')

def eliminar_tienda():
    nombre = input('Ingrese nombre de tienda: ')
    buscar_nombre_tienda(nombre)
    id_ingresado = input('Ingrese id de tienda para eliminar: ')
    tienda = tienda_por_id(id_ingresado)
    tienda.habilitado = False
    respuesta = guardar_tienda(tienda)
    if respuesta == 1:
        print(f'Tienda {tienda.nombre_tienda} eliminada con exito')

