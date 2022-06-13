##########################################################################
##						Mi primer juego - Ahorcado						##
##########################################################################
import getpass
print('\n\n')
print('BIENVENIDO AL AHORCADO','\n-----------------------------------------------------------------------------')
print('\n')
palabra = getpass.getpass('Ingrese la pablabra para el ahorcado: ')
print('\n')
cant = int(len(palabra))
palabraj1 = []
for letra in palabra:
    palabraj1.append(letra)

respuesta = []
for letra in palabra:
	respuesta.append('_')

# Recorro la lista para mostrar los valores
i = 0
while i != cant:
	print(respuesta[i],end = '')
	i = i + 1
else:
	pass

i = 0
while i<10:
	if respuesta.count('_') > 0:
		i = i + 1
		j = 0
		intento = input('\nIngrese una letra: ')
		print('\n')
		while j != cant:
			if palabra[j].upper() == intento.upper():
				respuesta[j] = intento.upper()
			j = j + 1
		else:
			pass
		m = 0
		while m < cant:
			print(respuesta[m], end = '')
			m = m + 1
		else:
			pass
		print('\n\n')
	else:
		i = 10
		print('\n#####################  GANASTE  #####################')
else:
	if respuesta.count('_') > 0:
		print('\n#####################   Fin del juego.. PERDISTE   #####################')


# Fin
#input('Pulse ENTER para finalizar con la ejecucion del juego del ahorcado.')