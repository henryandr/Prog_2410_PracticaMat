import pytest

def esquivarObstaculoYMover(matriz, fila_actual, columna_actual, obstaculo):
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
  # Implementar la lógica para comprobar el movimiento, esquivar el obstáculo y determinar la dirección
  ...

# Casos de prueba
def test_esquivarObstaculoYMover():
  matriz = [
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
  ]

  # Elemento en la posición (1, 1), con obstáculo en (2, 1)
  fila_nueva, columna_nueva = esquivarObstaculoYMover(matriz, 1, 1, (2, 1))
  assert fila_nueva == 0 and columna_nueva == 1  # Movimiento hacia arriba

  # Elemento en la posición (1, 1), con obstáculo en (2, 1)
  fila_nueva, columna_nueva = esquivarObstaculoYMover(matriz, 2, 1, (2, 1))
  assert fila_nueva == 2 and columna_nueva == 1  # Movimiento hacia abajo

  # Elemento en la posición (1, 1), con obstáculo en (1, 2)
  fila_nueva, columna_nueva = esquivarObstaculoYMover(matriz, 1, 1, (1, 2))
  assert fila_nueva == 1 and columna_nueva == 3  # Movimiento hacia la derecha

  # Elemento en la esquina superior izquierda, sin obstáculo
  fila_nueva, columna_nueva = esquivarObstaculoYMover(matriz, 0, 0, None)
  assert fila_nueva == 0 and columna_nueva == 1  # Movimiento hacia la derecha

  # Elemento en la esquina inferior derecha, sin obstáculo
  fila_nueva, columna_nueva = esquivarObstaculoYMover(matriz, 2, 3, None)
  assert fila_nueva == 2 and columna_nueva == 3  # No hay movimiento posible

  # Elemento en una posición sin obstáculo
  fila_nueva, columna_nueva = esquivarObstaculoYMover(matriz, 1, 2, None)
  assert fila_nueva == 1 and columna_nueva == 3  # Movimiento hacia la derecha (ejemplo)

  # Elemento en una posición con obstáculo en todas las direcciones
  fila_nueva, columna_nueva = esquivarObstaculoYMover(matriz, 1, 2, (2, 1), None)
  assert fila_nueva == 1 and columna_nueva == 2  # No hay movimiento posible

  # Obstáculo en la misma posición que el elemento
  fila_nueva, columna_nueva = esquivarObstaculoYMover(matriz, 1, 1, (1, 1))
  assert fila_nueva == 1 and columna_nueva == 1  # No hay movimiento posible

  # Obstáculo fuera de los límites de la matriz
  fila_nueva, columna_nueva = esquivarObstaculoYMover(matriz, 1, 1, (5, 5))
  assert fila_nueva == 1 and columna_nueva == 1  # No hay movimiento posible (obstáculo ignorado)

