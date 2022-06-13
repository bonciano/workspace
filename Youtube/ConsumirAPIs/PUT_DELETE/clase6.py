# Taller consumir APIs con Python - Metodo PUT y DELETE
import requests
import json

if __name__ == '__main__':
    
    url = 'http://httpbin.org/put'
    #url = 'http://httpbin.org/delete'
    
    payload = { 'Nombre' : 'Carlos', 'Curso' : 'Apis con Python', 'Nivel' : 'Intermedio' }
    headers = { 'Content-Type' : 'application/json' , 'Access-Token' : 'asdasd-asd-asd-adsddd' } 
    
    response = requests.put(url, data=json.dumps(payload), headers=headers)
    #response = requests.delete(url, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        # print(response.content)
        headers_response = response.headers # Diccionario
        print(headers_response)
        #Obtengo del header que me envia el servidor, el diccionario Server.
        server = headers_response['Server']
        print(server)

# GET para obtener algun recurso
# POST para crear un recurso
# PUT para actualizar un recurso
# DELETE para elminiar un recurso
# Nos son los unicos metodos HTTP, pero son los principales con los que podemos crear un CRUD completo.
