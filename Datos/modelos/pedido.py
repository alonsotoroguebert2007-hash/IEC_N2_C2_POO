from Datos.conexion import base_datos
from peewee import Model, AutoField, CharField, IntegerField, SQL, DateField

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Pedido(BaseModel):
    estado = CharField(constraints=[SQL("DEFAULT 'Creando'")], max_length=30)
    fecha = DateField(constraints=[SQL("DEFAULT curdate()")], null=True)
    id_pedido = AutoField()
    id_tienda = IntegerField(index=True, null=True)
    id_usuario = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'pedido'
