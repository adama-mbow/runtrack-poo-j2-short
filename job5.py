class Forme:
    def aire(self, aire = 0):
        self.aire = aire

class Rectangle(Forme):
    def __init__(self,longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur 

class Cercle(Forme):
    def __init__(self,radius):
        self.radius = radius

    def aire(self):
        return self.radius**2 * 3.14


rectangle = Rectangle(6, 15)
print(rectangle.aire())
cercle = Cercle(8)
print(cercle.aire())