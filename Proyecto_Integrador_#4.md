
1. Implementar una función que reciba el mapa de un laberinto en forma de cadena, y lo convierta a matriz de caracteres.
   i. Utiliza el siguiente mapa:
 
 laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

   ii. Los puntos inicial y final deben ser dados al crear el juego, usar las coordenadas (0,0) para el inicio y 
    (len(mapa)-1, len(mapa[0])-1) para el final.
   iii. Recuerdo: Para separar por filas usar split("\n") y para convertir una cadena a una lista de caracteres usar 
     list(cadena).
2.  Escribir una función que limpie la pantalla y muestre la matriz (recibe el mapa en forma de matriz)

3.  Implementar el main loop en una función (recibe el mapa en forma de matriz)
   i. recibir: mapa List[List[str]], posicion inicial Tuple[int, int], posicion final Tuple[int, int].
  ii. definir dos variavles px y py que contienen las coordenadas del jugador, iniciar como los valores de la posición incial
 iii. procesar mientras (px, py) no coincida con la coordenada final.
    a. asignar el caracter P en el mapa a las coordenadas (px, py) en todo momento.
    b. leer del teclado las teclas de flechas, antes de actualizar la posición, verificar si esta posición tentativa:
      a. No se sale del mapa
      b. No es una pared
    c. Si la nueva posición es válida, actualizar (px, py), poner el caracter P en esta nueva coordenada y restaurar la anterior a .
    d. mostrar
