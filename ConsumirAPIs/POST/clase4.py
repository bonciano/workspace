# Taller consumir APIs con Python - POST
# En el metodo POST, no se le puede hacer una peticion desde el navegador directamente, sino desde un script.
# Con el metodo POST se puede visualizar mas atributos que con GET
import requests
import json

if __name__ == '__main__':
    
    url = 'http://httpbin.org/post'
    payload = { 'Nombre' : 'Carlos', 'Curso' : 'Apis con Python', 'Nivel' : 'Intermedio' }
    
    # Forma 1 - json
    #response = requests.post(url, json = payload)

    # Forma 2 - data
    response = requests.post(url, data=json.dumps(payload))

    if response.status_code == 200:
        print(response.content)