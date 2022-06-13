# Taller consumir APIs con Python - GET
import requests

if __name__ == '__main__':
    
    url = 'http://www.google.com.ar'
    response = requests.get(url)

    if response.status_code == 200:
        content = response.content
        file = open('google.html', 'wb')
        file.write(content)
        file.close()
