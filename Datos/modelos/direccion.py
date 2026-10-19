from Datos.conexion import base_datos
from peewee import Model, AutoField, CharField, IntegerField

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Direccion(BaseModel):
    calle = CharField(max_length=20, null=True)
    ciudad = CharField(max_length=100, null=True)
    id_direccion = AutoField()
    id_usuario = IntegerField(index=True, null=True)
    num_postal = IntegerField(null=True)
    pais = CharField(max_length=100, null=True)
    region = CharField(max_length=100, null=True)

    class Meta:
        table_name = 'direccion'


