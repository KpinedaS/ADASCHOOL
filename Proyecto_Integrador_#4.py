
# Permite limpieza de pantalla y permitir lectura de teclas presionadas
import os
from readchar import readkey,key

#  Divide el laberinto en filas y lo  convierte en una matria de caracteres.
def convertir_laberinto(laberinto):
    #for fila in laberinto.split("\n"):
        #print(list(fila))
    return [list(fila) for fila in laberinto.split("\n")]

# define la  funcion para limpiar la pantalla.
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

#Funcion que muestra el mapa del laberinto y lo imprime linea por linea
def mostrar_mapa(mapa):
    for fila in mapa:
        print(''.join(fila))

# Inicia un bucle mientras la posicion iniciaal no coincida con la posicion final, en cada iteracion marca
# la posicion 'P' en el mapa,limpia y actualiza la pantalla, lee la entrada del usuario para mover al jugador
# verifica si es valido el movimiento, es decir que no salga del mapa y choque con paredes, actualiza coordenadas
#  Al terminar el bucle maraca la  posicion final de 'P', muestra el mapa final y el mensaje de "Ganaste"
def main_loop(mapa, posicion_inicial, posicion_final):
    px, py = posicion_inicial

    while (px, py) != posicion_final:
        limpiar_pantalla()
        mapa[px][py] = 'P'
        mostrar_mapa(mapa)
        mapa[px][py] = '.'

        tecla = readkey()
        if tecla == key.UP and px > 0 and mapa[px - 1][py] != '#':
            px -= 1  # Flecha arriba
        elif tecla == key.DOWN and px < len(mapa) - 1 and mapa[px + 1][py] != '#':
            px += 1  # Flecha abajo
        elif tecla == key.LEFT and py > 0 and mapa[px][py - 1] != '#':
            py -= 1  # Flecha izquierda
        elif tecla == key.RIGHT and py < len(mapa[0]) - 1 and mapa[px][py + 1] != '#':
            py += 1  # Flecha derecha
    print ("Ganaste")

    
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

# configura el escenario inicial del juego del laberinto definiendo mapa, posicion inicial y final.
mapa = convertir_laberinto(laberinto)
posicion_inicial = (0, 0)
posicion_final = (len(mapa) - 1, len(mapa[0]) - 1)
main_loop(mapa, posicion_inicial, posicion_final)