class Joueur:
    def __init__(self):
        self.__oxygene = 48
        self.__inventaire = {}

    def oxygene(self):
        return self.__oxygene

    def inventaire(self):
        return tuple(self.__inventaire)

    def vivant(self):
        return self.__oxygene > 0

    def consommer(self, cout):
        if cout < 0:
            raise ValueError("Cout negatif Interdit")
        self.__oxygene = max(0, self.oxygene - cout)
        return self.vivant

    def recharger(self):
        if self.vivant():
            self.__oxygene = min(80, self.oxygene + 30)

    def possede(self, nom):
        return nom in self.__inventaire

    def ajouter(self, objet):
        if not self.possede(objet.nom):
            self.__inventaire[objet.nom] = objet  

    def retirer(self, nom):
        return self.__inventaire.pop(nom, None)                  