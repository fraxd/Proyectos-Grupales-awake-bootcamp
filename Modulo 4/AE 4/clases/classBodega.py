class Bodega():
    Stock: 50000

    def descontarStock(self, stock):
        self.Stock -= stock
        return self.Stock
