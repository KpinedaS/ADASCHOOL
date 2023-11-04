# bibliotecas para opeeraciones con el sistema de archivos, para manejar las teclas en tiempo real.
import os
import random
from readchar import readkey, key

# Para situaciones en las que no hay archivos en la carpeta mapas.
class NotFileError(Exception):
    pass

# Defino el constructor que toma el laberinto como entrada y lo convierte en una matriz de caracteres,  
class Juego:
    def __init__(self, laberinto):
        self.mapa = [list(fila.strip()) for fila in laberinto.split("\n")]

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_mapa(self):
        for fila in self.mapa:
            print(''.join(fila))
            
    # Bucle principal del juego
    def main_loop(self):
        px, py = (0, 0)
        while self.mapa[px][py] != 'E':
            self.limpiar_pantalla()
            self.mapa[px][py] = 'P'
            self.mostrar_mapa()
            self.mapa[px][py] = '.'
            tecla = readkey()
            if tecla == key.UP and px > 0 and self.mapa[px - 1][py] != '#':
                px -= 1  # Flecha arriba
            elif tecla == key.DOWN and px < len(self.mapa) - 1 and self.mapa[px + 1][py] != '#':
                px += 1  # Flecha abajo
            elif tecla == key.LEFT and py > 0 and self.mapa[px][py - 1] != '#':
                py -= 1  # Flecha izquierda
            elif tecla == key.RIGHT and py < len(self.mapa[0]) - 1 and self.mapa[px][py + 1] != '#':
                py += 1  # Flecha derecha
        print("¡Ganaste, felicitaciones!")

# Se encarga de cargar el mapa e inicia el  juego
class JuegoArchivo:
    def __init__(self, path_a_mapas):
        self.path_a_mapas = path_a_mapas

    def cargar_laberinto(self):
        try:
            lista_de_archivos = os.listdir(self.path_a_mapas)
            if not lista_de_archivos:
                raise NotFileError("No hay archivos en la carpeta de mapas.")
            nombre_archivo = random.choice(lista_de_archivos)
            path_completo = os.path.join(self.path_a_mapas, nombre_archivo)
            with open(path_completo, 'r') as archivo_mapa:
                return archivo_mapa.read()
        except FileNotFoundError:
            raise NotFileError("La carpeta de mapas no existe.")
    '''
        ..###################
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
        ###################..
    '''

    def iniciar_juego(self):
        laberinto = self.cargar_laberinto()
        juego = Juego(laberinto)
        juego.main_loop()

# verifica si el script se esta ejecutando como programa principal, se configura la ruta a la carppeta mapas y se 
# inicia el juego
if __name__ == "__main__":
    path_a_mapas = "/ruta/a/tu/carpeta/de/mapas"
    juego_archivo = JuegoArchivo(path_a_mapas)
    juego_archivo.iniciar_juego()
