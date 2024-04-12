from random import randint
import time

#Implementar función para buscar la posición del dron en la matriz
def buscarElemento(matriz, elemento):
    pass    #Borre esta línea y escriba aquí su código
"""
  Función que busca un elemento dentro de una matriz 3x4 y retorna sus coordenadas.
  Args:
    matriz: Matriz 3x4 que contiene los elementos a buscar.
    elemento: Elemento a buscar dentro de la matriz. Símbolo que usas para el dron
  Returns:
    Fila y columna del elemento encontrado.
    Si el elemento no se encuentra, retorna -1, -1.
"""
  
#Función que mueve el dron a una posición correcta
def esquivarObstaculoYMover(matriz, fila_actual, columna_actual, obstaculo):
    pass    #Borre esta línea y escriba aquí su código
"""
  Función que comprueba si un elemento puede moverse esquivando un obstáculo y luego lo desplaza de forma horizontal o vertical (hacia la derecha, arriba o abajo). La dirección del movimiento se determina automáticamente.

  Args:
    matriz: Matriz 3x4 que representa el entorno.
    fila_actual: Fila actual del elemento.
    columna_actual: Columna actual del elemento.
    obstaculo: Tupla con las coordenadas (fila, columna) del obstáculo.

  Returns:
    Tupla con la nueva posición del elemento (fila_nueva, columna_nueva).
    Si el movimiento no es posible, retorna la posición actual.
"""
def destinoFinalDron(matriz, fila, columna):
    pass    #Borre esta línea y escriba aquí su código
"""
    Función que comprueba si el dron llegó a su destino final
    Args:
        matriz: Matriz 3x4 que representa el entorno.
        fila_actual: Fila actual del elemento.
        columna_actual: Columna actual del elemento.
    Returns:
        True: si el dron ya llegó
        False: si el dron aún no ha llegado 
"""


#Función que ubica el dron y el obstáculo en la matriz
def ubica_objetos(matriz):
    ind_fila = randint(0,2)
    ind_columna = randint(0,1)
    matriz[ind_fila][ind_columna] = '╬'
    matriz[ind_fila][ind_columna+1] = '▓'

#Función que imprime la matriz como una tabla con cada celda encerrada en un cuadro
def imprime_matriz(matriz):
    for i in range(len(matriz)):
        print('+---'*len(matriz[0])+'+')
        for j in range(len(matriz[i])):
            print(f'| {matriz[i][j]} ',end='')
        print('|')
    print('+---'*len(matriz[0])+'+')

#Función que crea la matriz y la llena con espacios vacíos
def crea_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(' ')
    return matriz

#Programa Principal
def main():
    #crea una matriz de 3x4
    matriz = crea_matriz(3,4)    
    ubica_objetos(matriz)
    imprime_matriz(matriz)


if __name__ == "__main__":
    main()