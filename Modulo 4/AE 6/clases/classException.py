class notFoundExcept(Exception):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f'{self.valor} no tiene suficiente stock'