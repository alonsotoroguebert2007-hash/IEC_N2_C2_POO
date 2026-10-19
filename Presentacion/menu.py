import sys
from Datos import nombre_app,version_app,main_menu
from Presentacion.presentacion_tienda import mostrar_tienda, datos_tienda, eliminar_tienda

def menu_principal():
    print(f'{nombre_app} {version_app}')
    print('='*len(nombre_app) + "=" + '='*len(version_app))

    while True:
        for clave,valor in main_menu.items():
            print(f'[{clave}] - {valor}')

        opcion_usuario = input('Ingrese una opción [1-4]: ')

        if opcion_usuario == '1':
            mostrar_tienda()
        elif opcion_usuario == '2':
            datos_tienda()
        elif opcion_usuario == '3':
            eliminar_tienda()
        elif opcion_usuario == '4':
            print('Saliendo de Sistema')
            sys.exit()
        else:
            print('Opción Ingresada NO corresponde...\nIngrese nuevamente.')