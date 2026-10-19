from Datos.conexion import base_datos
from peewee import Model, AutoField, CharField, IntegerField, SQL, TextField, DateTimeField

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Pago(BaseModel):
    estado = TextField(null=True)
    fecha = DateTimeField(constraints=[SQL("DEFAULT curdate()")], null=True)
    id_pago = AutoField()
    id_pedido = IntegerField(index=True, null=True)
    metodo_pago = CharField(max_length=10, null=True)
    monto = IntegerField(null=True)

    class Meta:
        table_name = 'pago'