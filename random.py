import random
import time
import os

numeroAleatorio = random.randint(1,100)
print(numeroAleatorio)

def limpiarPantalla():
    os.system("cls")
def tiempo():
    time.sleep(2)
    
def numeroElegido(numero):
    for i in range(8):
        limpiarPantalla()
        try:
            print(f"Tienes 7 intentos para adivinar el número secreto, llevas {i} intentos")
            numero = int(input("\nIngresa un número del 1 al 100: "))
            if numero < numeroAleatorio:
                print("Tu número es menor que el número secreto")
                tiempo()
            elif numero > numeroAleatorio:
                print("Tu número es mayor que el número secreto")
                tiempo()
            elif numero == numeroAleatorio:
                print("Has adivinado el número secreto... ¡Felicidades!")
                tiempo()
                break
        except ValueError:
            print("Debes ingresar un número, vuelve a intentar")
            tiempo()
        print("Has agotado tus intentos... Ha perdido el juego :(")
    
numeroElegido(any)
        