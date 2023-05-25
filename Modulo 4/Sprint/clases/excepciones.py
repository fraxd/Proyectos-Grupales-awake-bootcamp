class SkuNotFound(Exception):
    def __init__(self, sku):
        self.sku = sku
    
    def __str__(self):
        return f"El SKU '{self.sku}' seleccionado no existe en el registro"
    
class stockInsuficient(Exception):
    def __init__(self, sku):
        self.sku = sku
    
    def __str__(self):
        return f"El SKU '{self.sku}' seleccionado no tiene stock suficiente."