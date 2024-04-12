# Casos de prueba
from src.practicaMat import buscarElemento
import pytest 

def test_buscarElemento():
  matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
  ]

  # Elemento presente en la matriz
  fila, columna = buscarElemento(matriz, 6)
  assert fila == 1 and columna == 1

  # Elemento no presente en la matriz
  fila, columna = buscarElemento(matriz, 15)
  assert fila == -1 and columna == -1

  # Casos borde: elemento en la esquina superior izquierda, inferior derecha
  fila, columna = buscarElemento(matriz, 1)
  assert fila == 0 and columna == 0

  fila, columna = buscarElemento(matriz, 12)
  assert fila == 2 and columna == 3

  # Casos borde: elemento en la primera fila, última columna
  fila, columna = buscarElemento(matriz, 4)
  assert fila == 0 and columna == 3

  fila, columna = buscarElemento(matriz, 12)
  assert fila == 2 and columna == 3

