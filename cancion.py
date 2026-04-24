class Cancion:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor

    @property
    def get_titulo(self):
        return self._titulo

    @property
    def get_autor(self):
        return self._autor

    def set_titulo(self, titulo: str):
        self._titulo = titulo

    def set_autor(self, autor: str):
        self._autor = autor