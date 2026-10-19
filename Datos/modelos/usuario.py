from Datos.conexion import base_datos
from peewee import Model, AutoField, CharField, IntegerField, DateField, CharField

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Usuario(BaseModel):
    contrasena =  CharField(max_length=200)
    correo = CharField(max_length=100, null=True)
    fecha_nac = DateField(null=True)
    id_usuario = AutoField()
    nombre = CharField(max_length=50)
    rut = IntegerField()
    telefono = IntegerField(null=True)

    class Meta:
        table_name = 'usuario'