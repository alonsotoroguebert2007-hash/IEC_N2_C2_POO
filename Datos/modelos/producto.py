from Datos.conexion import base_datos
from peewee import Model, AutoField, CharField, IntegerField

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Producto(BaseModel):
    categoria = CharField(max_length=250, null=True)
    descripcion = CharField(null=True)
    id_producto = AutoField()
    id_tienda = IntegerField(index=True, null=True)
    imagen = CharField(null=True)
    nombre = CharField(max_length=200, null=True)
    precio = IntegerField(null=True)
    stock = IntegerField(null=True)

    class Meta:
        table_name = 'producto'
