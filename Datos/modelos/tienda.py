from Datos.conexion import base_datos
from peewee import Model, AutoField, CharField, IntegerField, DateTimeField, BooleanField

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Tienda(BaseModel):
    correo = CharField(max_length=100)
    estado = CharField(max_length=20, null=True)
    horario_atencion = DateTimeField()
    id_tienda = AutoField()
    nombre = CharField(max_length=50)
    telefono = IntegerField()
    habilitado = BooleanField()

    class Meta:
        table_name = 'tienda'