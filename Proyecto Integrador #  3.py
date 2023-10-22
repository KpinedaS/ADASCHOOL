# Lee un caracter o una pulsacion de tecla y funcionalidades del sistema operativo
from  readchar import readkey, key
import os
def borrar_pantalla(): # definimos  la funcion para borrar la pantalla
    os.system('cls' if os.name =='nt' else 'clear') 
    
def imprimir_numero(contador): # definimos la funcion del contador
    print(contador)
numero=0
print("!Como estas amigo! si quieres jugar presiona la tecla n")  # al iniciar programa imprime mensaje inicial.

while True: # evalua la condicion con la tecla n, siempre y cuando se presione la tecla
    tecla = readkey()
    if tecla=="n": 
        borrar_pantalla()
        imprimir_numero(numero)
        if numero ==50: # si se presiona la tecla n imprime el numero y limpia la pantalla 
            print("Has llegado a 50, es el fin del juego")
            break # cuando  llega a 50 imprime el mensaje y sale del programa
        numero = numero + 1  # va sumando el numero que imprime en pantalla

