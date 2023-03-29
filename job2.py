class Personne:
    def __init__(self, age = 14):
        self.age = age

    def afficherAge(self):
        age = self.age
        print("l'age de la personne est: ", self.age, "ans")

    def bonjour(self):
        print("Hello")

    def setAge(self, age):
        self.age = age

class Eleve(Personne):
    def __init__(self, age = 14):
        Personne.__init__(self, age)

    def allerEnCours(self):
        print("je vais en cours")


class Professeur(Personne):
    def __init__(self, __matiereEnseignee):
        self.__matiereEnseignee = __matiereEnseignee

    def __str__(self):
        return f"Professeur {self.__matiereEnseignee}"

    def enseigner(self):
        print("le cours va commencer.")

personne = Personne()
eleve = Eleve()
prof = Professeur("math")
eleve.bonjour()
eleve.allerEnCours()
eleve.setAge(15)
eleve.afficherAge()
prof.bonjour()
prof.enseigner()
