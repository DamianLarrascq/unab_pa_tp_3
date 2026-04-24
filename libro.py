class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


class Libro:
    def __init__(self):
        self._titulo: str = ''
        self._autor: Persona = Persona('')
        self._ISBN: str = ''
        self._paginas: int = 0
        self._edicion: str = ''
        self._editorial: str = ''
        self._lugar: str = ''
        self._fecha: str = ''

    @property
    def get_titulo(self) -> str:
        return self._titulo

    @property
    def get_autor(self) -> Persona:
        return self._autor.nombre

    @property
    def get_isbn(self) -> str:
        return self._ISBN

    @property
    def get_paginas(self) -> int:
        return self._paginas

    @property
    def get_edicion(self) -> str:
        return self._edicion

    @property
    def get_editorial(self) -> str:
        return self._editorial

    @property
    def get_lugar(self) -> str:
        return self._lugar

    @property
    def get_fecha(self) -> str:
        return self._fecha

    def set_titulo(self, titulo: str):
        self._titulo = titulo

    def set_autor(self, autor: str):
        self._autor = Persona(autor)

    def set_isbn(self, isbn: str):
        self._ISBN = isbn

    def set_paginas(self, paginas: int):
        self._paginas = paginas

    def set_edicion(self, edicion: str):
        self._edicion = edicion

    def set_editorial(self, editorial: str):
        self._editorial = editorial

    def set_lugar(self, lugar: str):
        self._lugar = lugar

    def set_fecha(self, fecha: str):
        self._fecha = fecha

    def __str__(self):
        return (f'Titulo: {self.get_titulo}\n'
                f'Autor: {self.get_autor}\n'
                f'ISBN: {self.get_isbn}\n'
                f'{self.get_lugar}\n'
                f'{self.get_fecha}\n'
                f'{self.get_paginas} paginas')

libro1 = Libro()
libro1.set_titulo('Introduction to Java Programming 3a. edicion')
libro1.set_autor('Liang, Y. Daniel')
libro1.set_isbn('0-13-031997-X')
libro1.set_lugar('Prentice-Hall, New Jersey (USA)')
libro1.set_fecha('viernes 16 de noviembre de 2001')
libro1.set_paginas(784)

print(libro1.__str__())