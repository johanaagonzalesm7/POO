class Esquinero():
    Color = "Nogal"
    Altura = "1.90 cm"
    Clasificacion = "Mueble Clasico"
    TipoDeMadera = "Cedro Rojo"
    Vidrio = "True"

    def EsquineroAlmacena(self):
        print("Se guardan objetos relevantes")
        pass
    def EsquineroMuestra(self):
        print("Se da a conocer cosas importantes")
        pass

EsquineroA = Esquinero()
EsquineroA.EsquineroAlmacena()
EsquineroA.EsquineroMuestra()