import requests
import json

if __name__ == '__main__':
    
    url = 'https://cafecito.app/post'
    payload = { 'Nombre' : 'Carlos'}
    headers = { 'Content-Type' : 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        # print(response.content)
        headers_response = response.headers # Diccionario
        print(headers_response)
        #Obtengo del header que me envia el servidor, el diccionario Server.
        #server = headers_response['Server']
        #print(server)
