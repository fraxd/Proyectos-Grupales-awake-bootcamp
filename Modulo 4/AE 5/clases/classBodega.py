class Bodega():
    Stock: int

    def __init__(self) -> None:
        self.Stock = 5000
        pass
        
    def descontarStock(self, desc):
        self.Stock -= desc
        return self.Stock
