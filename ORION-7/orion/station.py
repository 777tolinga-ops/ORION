
from joueur import Joueur
from salle import Salle
from enigme import EnigmeObjet, EnigmeCode


class StationManager:

    def __init__(self):
        self.joueur = Joueur()
        self.salles = {
            "sas": Salle("sas", ["réserve", "laboratoire"]),
            "réserve": Salle("réserve", ["sas"], ["badge", "câble"]),
            "laboratoire": Salle("laboratoire", ["sas", "machines"], ["fusible", "bonbonne"]),
            "machines": Salle("machines", ["laboratoire", "commande"]),
            "commande": Salle("commande", ["machines"])
        }

        self.position = "sas"
        self.maintenance = False
        self.installes = set()
        self.reacteur = False
        self.victoire = False
        self.code = "4729"
        self.enigmes = {
            "badge": EnigmeObjet("badge"),
            "code": EnigmeCode(self.code)
        }

    def terminee(self):
        if self.victoire or not self.joueur.vivant():
            return True
        return False

    def payer(self, cout):
        if self.terminee():
            return False

        return self.joueur.consommer(cout)

    def passage(self, destination):
        salle = self.salles[self.position]

        if destination not in salle.sorties:
            return False

        if destination == "machines" or self.position == "machines":
            if destination == "laboratoire" or self.position == "laboratoire":
                return self.maintenance
            if destination == "commande" or self.position == "commande":
                return self.reacteur

        return True

    def etat(self):
        sorties = []
        for destination in self.salles[self.position].sorties:
            if self.passage(destination):
                sorties.append(destination)
            else:
                sorties.append(destination + " (verrouillée)")

        return f"Salle : {self.position} | Oxygène : {self.joueur.oxygene()}/80 | Sorties : {', '.join(sorties)}"

    def resoudre(self, nom, reponse=""):
        enigme = self.enigmes[nom]
        return enigme.verifier(self.joueur, reponse)

    def deplacer(self, destination):
        if not self.passage(destination):
            return "Passage impossible."
        if not self.payer(6):
            return "Plus d'oxygène."

        self.position = destination
        return f"Vous êtes dans la salle {destination}."

    def observer(self):
        if not self.payer(1):
            return "Plus d'oxygène."

        salle = self.salles[self.position]
        objets = ", ".join(salle.objets)

        if not objets:
            objets = "Aucun objet"

        return f"{self.etat()}\nObjets : {objets}\nRéacteur : {self.reacteur}\nPièces installées : {', '.join(self.installes)}"

    def journal(self):
        if self.position != "laboratoire":
            return "Vous devez être au laboratoire."

        if not self.payer(1):
            return "Plus d'oxygène."

        return f"Le code du réacteur est : {self.code}"

    def ramasser(self, nom):
        salle = self.salles[self.position]

        if not salle.contient(nom):
            return "Objet absent."

        if self.joueur.possede(nom):
            return "Objet déjà possédé."

        if not self.payer(2):
            return "Plus d'oxygène."

        objet = salle.prendre(nom)
        self.joueur.ajouter(objet)

        return f"{nom} ramassé."

    def utiliser(self, nom):
        if not self.joueur.possede(nom):
            return "Objet absent de l'inventaire."

        if nom == "badge":
            if self.position != "laboratoire":
                return "Utilisation impossible ici."

            if self.maintenance:
                return "Porte déjà ouverte."

            if not self.resoudre("badge"):
                return "Badge incorrect."

            if not self.payer(2):
                return "Plus d'oxygène."

            self.maintenance = True
            return "Porte de maintenance ouverte."

        elif nom == "câble" or nom == "fusible":
            if self.position != "machines":
                return "Vous devez être dans les machines."
            if nom in self.installes:
                return "Objet déjà installé."
            if not self.payer(2):
                return "Plus d'oxygène."

            self.installes.add(nom)
            self.joueur.retirer(nom)

            return f"{nom} installé."

        elif nom == "bonbonne":
            if not self.payer(2):
                return "Plus d'oxygène."

            self.joueur.recharger()
            self.joueur.retirer(nom)

            return "Oxygène rechargé."

        else:
            return "Utilisation impossible."

    def tenter_code(self, reponse):
        if self.position != "machines":
            return "Vous devez être dans les machines."

        if self.reacteur:
            return "Réacteur déjà actif."

        if "câble" not in self.installes:
            return "Le câble doit être installé."

        if "fusible" not in self.installes:
            return "Le fusible doit être installé."

        if not self.payer(3):
            return "Plus d'oxygène."

        if self.resoudre("code", reponse):
            self.reacteur = True
            return "Réacteur activé."

        return "Code incorrect."

    def attendre(self):
        if not self.payer(5):
            return "Plus d'oxygène."

        return "Vous avez consommé 5 unités d'oxygène."

    def evacuer(self):
        if self.position != "commande":
            return "Vous devez être dans la commande."

        if not self.reacteur:
            return "Le réacteur doit être actif."

        if not self.payer(3):
            return "Plus d'oxygène."

        self.victoire = True

        return "Évacuation réussie."

