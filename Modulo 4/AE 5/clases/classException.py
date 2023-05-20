class notFoundExcept(Exception):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f'{self.valor} no tiene suficiente stock'
    
class insufficientStock(Exception):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f'{self.valor} no tiene suficiente stock'
    
class notMoney(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return f'Saldo Insuficiente para ejecutar compra.'
    