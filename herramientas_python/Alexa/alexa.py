################################################################
####################### Alexa con python #######################
################################################################
# Requisitos:
# instalar SpeechRecognition 
# instalar pyttsx3 
# instalar PyAudio
# pywhatkit ?
# Ver video tutorial: https://www.youtube.com/watch?v=8WKjX0dbh4E
################################################################

import speech_recognition as sr
import pyttsx3
import pywhatkit
#import urllib.request
#import json
import datetime
#import wikipedia

# Nombre del asistente virtual
name = 'paloma'

# API key --> https://console.developers.google.com/getting-started?pli=1
#key = 'YOUR_API_KEY_HERE'

# Este flag sirve para apagar el programa
flag = 1

listener = sr.Recognizer()
engine = pyttsx3.init()

# Obtener voces (Se elige la primera de la lista [0])
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Se edita la configuracion
engine.setProperty('rate', 178)
engine.setProperty('volume', 0.7)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    flag = 1
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()

            if name in rec:
                rec = rec.replace(name, '')
                flag = run(rec)
            else:
                talk("Vuelva a intentarlo, no entiendo la solicitud...")
    except:
        pass
    return flag

def run(rec):
    if 'reproducir' in rec:
        music = rec.replace('reproducir', '')
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music)
    # elif 'cuantos suscriptores tiene' in rec:
    #     name_subs = rec.replace('cuantos suscriptores tiene', '')
    #     data = urllib.request.urlopen(f'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={name_subs.strip()}&key={key}').read()
    #     subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    #     talk(name_subs + " tiene {:,d}".format(int(subs)) + " suscriptores!")
    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
    # elif 'busca' in rec:
    #     order = rec.replace('busca', '')
    #     wikipedia.set_lang("es")
    #     info = wikipedia.summary(order, 1)
    #     talk(info)
    elif 'salir' in rec:
        flag = 0
        talk("Saliendo...")

    else:
        talk('No encontre lo que buscabas...')
    return flag

while flag:
    flag = listen()
