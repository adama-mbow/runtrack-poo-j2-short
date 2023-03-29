class Personne:
    def __init__(self, age = 14):
        self.age = age

    def afficherAge(self):
        age = self.age
        print("l'age de la personne est: ", self.age, "ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        self.age= age
        print("l'age de la personne est: ", self.age, "ans")

class Eleve(Personne):
    def __init__(self, age = 14):
        Personne.__init__(self, age)

    def allerEnCours(self):
        print("je vais en cours")


class Professeur:
    def __init__(self, __matiereEnseignee):
        self.__matiereEnseignee = __matiereEnseignee

    def __str__(self):
        return f"Professeur {self.__matiereEnseignee}"

    def enseigner(self):
        print("le cours va commencer.")

personne = Personne()
eleve = Eleve()
eleve.allerEnCours()
eleve.afficherAge()
enseingnement = Professeur("mathematique")
enseingnement.enseigner()
print(enseingnement)
print(personne())


