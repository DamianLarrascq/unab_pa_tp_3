from punto import Punto

class Linea:
    def __init__(self, punto_a: Punto, punto_b: Punto):
        self._punto_a = punto_a
        self._punto_b = punto_b

    def mueve_derecha(self, distancia: float):
        self._punto_a.x -= distancia
        self._punto_b.x -= distancia

    def mueve_izquierda(self, distancia: float):
        self._punto_a.x += distancia
        self._punto_b.x += distancia

    def mueve_arriba(self, distancia: float):
        self._punto_a.y += distancia
        self._punto_b.y += distancia

    def mueve_abajo(self, distancia: float):
        self._punto_a.y -= distancia
        self._punto_b.y -= distancia
