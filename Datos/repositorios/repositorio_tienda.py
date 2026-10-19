from Datos.conexion import base_datos
from Datos.modelos.tienda import Tienda
from Datos.auxiliar import mensaje_error_orm

database = base_datos

def listado_tienda():
    tienda = Tienda.select().where(Tienda.habilitado == True)
    return tienda

def guardar_tienda(tienda: Tienda):
    try:
        tienda_nueva = tienda.save()
        return tienda_nueva
    except Exception as error:
        print(f'{mensaje_error_orm} {error}')

def tienda_por_nombre(tienda_nombre):
    try:
     tienda = Tienda.select().where(Tienda.nombre.contains(tienda_nombre), Tienda.habilitado == True)
     if tienda:
         return tienda
    except Exception as error:
        print(f'Ha ocurrido un error {error}')

def tienda_por_id(id):
    try:
        tienda = Tienda[id]
        if tienda:
            return tienda
    except Exception as error:
        print(f'Ha ocurrido un error {error}')
