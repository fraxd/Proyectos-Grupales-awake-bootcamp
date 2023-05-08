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

vendedor1 = Vendedor('17888111-1', 'Pablo', 'Picasso', 'Zapatillas')
vendedor2 = Vendedor('18999666-9', 'Vincent', 'Vangoh', 'Poleras' )
vendedor3 = Vendedor("33333333-3", "Marcela", "Torres", "Zapatos")
vendedor4 = Vendedor("44444444-4", "Santiago", "Sánchez", "Poleron")
vendedor5 = Vendedor("55555555-5", "Lucía", "González", "Chaqueta")