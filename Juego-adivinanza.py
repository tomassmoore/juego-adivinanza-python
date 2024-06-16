
import random

numero_secreto = random.randint(0,99)
cantidad_intentos= 0
cantidad_max_intentos= 5
adivinado = False

print('Bienvenido al juego! Vas a tener que adivinar el numero secreto!')

while not adivinado and cantidad_intentos < cantidad_max_intentos:
    entrada = input('Introduce un numero del 1 al 99: ') 
    numero = int(entrada)

    if numero == numero_secreto:
        print('Ganaste! El numero era: ',numero_secreto)
        adivinado = True
    elif numero < numero_secreto:
        print ('El numero es mayor al ingresado')
    else:
        print('El numero es menor al ingresado')

    cantidad_intentos += 1
   
    if not cantidad_intentos < cantidad_max_intentos:
        print('Game over. No has podido adivinar dentro de los 10 intentos')