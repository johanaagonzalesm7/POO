class carro:
    Color = "Azul"
    Modelo = "Jetta"
    Placa = "JAG-037"
    Tamaño = "Mediano"
    Kilometraje = "11306"
    Alarma = "True"

    def EnciendeCarro(self):
        print("El auto esta encendido")
        pass
    def ApagaCarro(self):
        print("El auto esta apagado")
        pass
    def AvanzaCarro(self):
        print("El auto esta avanzado")
        pass
    def ParaCarro(self):
        print("El auto esta parado")
        pass
    def PitaCarro(self):
        print("El auto esta pitando por una sola vez")
        pass

CarroJohana = carro()
CarroJohana.EnciendeCarro()
CarroJohana.ApagaCarro()
CarroJohana.AvanzaCarro()
CarroJohana.ParaCarro()
CarroJohana.PitaCarro()
