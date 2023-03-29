class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        print ((self.__longueur + self.__largeur)*2)

    def surface(self):
        print(self.__longueur * self.__largeur)

    def get_longueur(self):
        return self.__largeur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur

class Parallélépipède(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.__longueur * self.__largeur * self.__hauteur
       
        

geometrie = Rectangle(14, 6)
parallélépipède = Parallélépipède(14,6,5)
geometrie.perimetre()
geometrie.surface()
print(parallélépipède.volume())

