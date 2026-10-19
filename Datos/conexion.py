from decouple import config
from peewee import MySQLDatabase

def base_datos():
    conexion = MySQLDatabase(config('db'), **{
        'charset': 'utf8mb4', 
        'host': config('host'), 
        'port': config('port', cast=int), 
        'user': config('user'), 
        'password': config('password')})
    return conexion