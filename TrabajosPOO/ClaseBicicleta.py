from msilib.schema import Class


class Bicicleta:
    TamañoDeLlanta = "26"
    TamañoDeMarco = "Grande"
    Material = "Aluminio"

    def BiciletaCambio(self):
        print("Realiza cambios la bicicleta")
        pass
    def BicicletaMover(self):
        print("Se mueve la bicicleta")
        pass
    def BicicletaFrena(self):
        print("Realiza la accion de frenar")
        pass

BicicletaJ = Bicicleta()
BicicletaJ.BicicletaMover()
BicicletaJ.BiciletaCambio()
BicicletaJ.BicicletaFrena()