from Datos.conexion import base_datos
from peewee import Model, AutoField, CharField, IntegerField, TextField, DateTimeField, SQL

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Envio(BaseModel):
    costo = IntegerField()
    estado = TextField(null=True)
    fecha_entrega = DateTimeField(constraints=[SQL("DEFAULT curdate()")], null=True)
    fecha_envio = DateTimeField(constraints=[SQL("DEFAULT curdate()")], null=True)
    id_direccion = IntegerField(index=True, null=True)
    id_envio = AutoField()
    id_pedido = IntegerField(index=True, null=True)
    num_seguimiento = IntegerField()
    transporte = CharField(max_length=15, null=True)

    class Meta:
        table_name = 'envio'