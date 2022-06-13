# Taller consumir APIs con Python - GET
# Si se usa una peticion del tipo GET, todos los parametros tienen que ir en la URL

import requests

if __name__ == '__main__':
    
    url = 'http://httpbin.org/get'
    args = {'Nombre' : 'Carlos', 'Curso' : 'Apis con Python'}
    response = requests.get(url, params=args) #se le coloca params para pasarle un diccionario como valores a enviar
    print(response.url)

    if response.status_code == 200:
        content = response.content
        print(content)
 