class Enigme:
     def verifier(self, joueur, reponse):
        raise NotImplementedError("À définir dans la classe fille")

class EnigmeObjet:
    def __init__(self, objet):
        self.objet = objet
    def verifier(self, joueur, reponse):
        return joueur.possede(self.objet)

class EnigmeCode(Enigme):
    def __init__(self, code):
        self.__code = code
    def verifier(self, joueur, reponse):
        return reponse == self.__code    