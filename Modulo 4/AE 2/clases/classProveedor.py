class proveedor():
    rut = str  # Basicamente es numero de rut sin puntos, Solo con -
    nombreLegal = str
    razonSocial = str
    direccion = str
    pais = str
    personaJuridica = bool #True = Persona Juridica | False = Persona Natural

    def __init__(self, rut, nombreLegal, razonSocial, pais, personaJuridica, direccion =''):
        self.rut = rut
        self.nombreLegal = nombreLegal
        self.razonSocial = razonSocial
        self.pais = pais
        self.personaJuridica = personaJuridica
        self.direccion = direccion

    