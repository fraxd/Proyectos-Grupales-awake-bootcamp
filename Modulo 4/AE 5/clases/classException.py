class notFoundExcept(Exception):
    def __init__(self, valor):
        self.valor = valor