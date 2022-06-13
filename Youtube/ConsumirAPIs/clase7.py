# Taller consumir APIs con Python - Chunks
import requests
import json

if __name__ == '__main__':
    url = 'https://wallpapers.com/images/high/angry-sea-dragon-hiiv4o2mkpu7x492.jpg'
    
    response = requests.get(url, stream=True)