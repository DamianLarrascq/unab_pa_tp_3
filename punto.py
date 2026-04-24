class Punto:
    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y

    def eje_x(self):
        return self.x

    def eje_y(self):
        return self.y

    def impresion(self):
        print(f'Eje x: {self.eje_x()} \nEje y: {self.eje_y()}')

    def opuesto(self):
        return -self.x, -self.y
