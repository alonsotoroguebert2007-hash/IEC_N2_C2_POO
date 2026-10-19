from Datos.conexion import base_datos
from peewee import Model, AutoField, IntegerField

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class DetallePedido(BaseModel):
    cantidad = IntegerField(null=True)
    id_detalle = AutoField()
    id_pedido = IntegerField(index=True, null=True)
    id_producto = IntegerField(index=True, null=True)
    precio_unitario = IntegerField(null=True)
    sub_total = IntegerField(null=True)

    class Meta:
        table_name = 'detalle_pedido'