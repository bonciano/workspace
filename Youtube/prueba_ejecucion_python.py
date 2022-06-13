print('Iniciando tareas de mantenimiento..\n')
clave = input('Password: ')
inicio = input('Iniciar con el mantenimiento?: (y/n)')

def tarea_diaria(inicio, clave):
    if clave == 12321:
        if inicio == 'y':
            print('***** Update del Sistema Operativo *****')
        else:
            print('No se realizaron mantenimiento sobre el equipo.')

tarea_diaria(inicio, clave)

