class Vehicule:
    def __init__(self, marque, année, prix):
        self.marque = marque
        self.année = année
        self.prix = prix

    def informations(self):
        print("Marque = ", self.marque)
        print("Prix = ",  self.prix, "euro")
        print("Année = ", self.année)

class Voiture(Vehicule):
    def __init__(self, marque, année, prix, porte = 4):
        super().__init__(marque, année, prix)
        self.porte = porte

    def informations(self):
        #return f"{super().informations()} {self.porte}
        print(super().informations())
        print("porte = ",self.porte)


class Moto(Vehicule):
    def __init__(self, marque, année, prix, roue = 2):
        super().__init__(marque, année, prix)
        self.roue = roue  

    def informations(self):
        #return f"{super().informations()} {self.porte}
        print(super().informations())
        print("roue = ",self.roue)

vehicule = Vehicule("Mercedes", 2020, 18500)
vehicule.informations()
voiture = Voiture("Mercedes", 2020, 18500, 4)
voiture.informations()
moto = Moto("yamaha", 1987, 4500, 2)
moto.informations()



