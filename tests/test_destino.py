# Casos de prueba
import pytest
from src.practicaMat import destinoFinalDron


def test_destinoFinalDron():
  matriz = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
  ]

  # Elemento en la última columna
  assert destinoFinalDron(matriz, 1, 3) == True

  # Elemento en una columna anterior a la última
  assert destinoFinalDron(matriz, 1, 2) == False

  # Elemento en la primera columna
  assert destinoFinalDron(matriz, 1, 0) == False

  # Elemento en la esquina superior izquierda
  assert destinoFinalDron(matriz, 0, 0) == False

  # Elemento en la esquina inferior derecha
  assert destinoFinalDron(matriz, 2, 3) == True

  # Elemento en la última fila, penúltima columna
  assert destinoFinalDron(matriz, 2, 2) == False

  # Elemento en la primera fila, última columna
  assert destinoFinalDron(matriz, 0, 3) == True