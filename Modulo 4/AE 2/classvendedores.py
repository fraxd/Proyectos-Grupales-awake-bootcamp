class Vendedor():
    run = str
    nombre = str
    apellido = str
    seccion = str
    
    def __init__(self, run, nombre, apellido, seccion):
            
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
    
    def getRun(self):
        return self.run


