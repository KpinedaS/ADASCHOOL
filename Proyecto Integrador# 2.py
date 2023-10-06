
# Escribir un programa que corra un bucle infinito leyendo e imprimiento las teclas 
# y sólo terminará cuando se presione la tecla ↑ indicada como UP

from readchar import readkey, key

while True:
   tecla=readkey()
   if tecla == key.UP:
      print("Finalisaste el programa, Hasta Luego.!!! ")
      break
   print(tecla)
