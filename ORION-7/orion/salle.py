class Objet:
    def __init__(self, nom):
        self.nom = nom

class Salle:
    def __init__(self, nom, sorties, objets=None):
        self.nom = nom
        self.sorties = sorties
        self.objets = {}
        if objets is not None:
            for nom_objet in objets:
                self.objets[nom_objet] = Objet(nom_objet)
    def contient(self, nom):
        return nom in self.objets
    def prendre(self, nom):
        return self.objets.pop(nom, None)

