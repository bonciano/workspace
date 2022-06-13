# Taller consumir APIs con Python - GET
# Obtener Json y seleccionar atributos particulares de ese archivo
import requests
import json

if __name__ == '__main__':
    
    url = 'http://httpbin.org/get'
    args = {'Nombre' : 'Carlos', 'Curso' : 'Apis con Python'}

    response = requests.get(url, params=args)
    # print(response)

    if response.status_code == 200:
        # Forma 1
        print(f'Forma 1')
        response_json = response.json() #Esta variable es un diccionario
        origin = response_json['origin']
        print(origin)
        
        # Forma 2
        print(f'Forma 2')
        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)

 