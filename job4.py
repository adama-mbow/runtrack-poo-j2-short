class Forme:
    def aire(self, aire = 0):
        self.aire = aire
        

class Rectangle(Forme):
    def __init__(self,longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur       



mesure = Rectangle(6, 15)
print(mesure.aire())
