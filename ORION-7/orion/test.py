
from station import StationManager
from joueur import Joueur
from salle import Salle
from enigme import EnigmeObjet, EnigmeCode


def test_joueur():
    joueur = Joueur()

    assert joueur.oxygene() == 48
    assert joueur.inventaire() == ()
    assert joueur.vivant() == True

    joueur.consommer(6)
    assert joueur.oxygene() == 42

    joueur.recharger()
    assert joueur.oxygene() == 72

    joueur.recharger()
    assert joueur.oxygene() == 80

    joueur.consommer(100)
    assert joueur.oxygene() == 0
    assert joueur.vivant() == False


def test_salle():
    salle = Salle("réserve", ["sas"], ["badge", "câble"])

    assert salle.contient("badge") == True
    assert salle.contient("fusible") == False

    salle.prendre("badge")

    assert salle.contient("badge") == False
    assert salle.prendre("badge") == None


def test_enigmes():
    joueur = Joueur()
    enigme = EnigmeCode("4729")

    assert enigme.verifier(joueur, "4729") == True
    assert enigme.verifier(joueur, "1234") == False

    enigme_badge = EnigmeObjet("badge")

    assert enigme_badge.verifier(joueur, "") == False


def test_deplacement():
    station = StationManager()

    assert station.position == "sas"

    station.deplacer("machines")

    assert station.position == "sas"
    assert station.joueur.oxygene() == 48

    station.deplacer("laboratoire")

    assert station.position == "laboratoire"
    assert station.joueur.oxygene() == 42

    station.deplacer("machines")

    assert station.position == "laboratoire"
    assert station.joueur.oxygene() == 42


def test_inventaire():
    station = StationManager()

    station.deplacer("réserve")
    station.ramasser("badge")

    assert station.joueur.possede("badge") == True
    assert station.joueur.oxygene() == 40

    station.ramasser("badge")

    assert station.joueur.oxygene() == 40
    assert station.joueur.inventaire() == ("badge",)


def test_bonbonne():
    station = StationManager()

    station.deplacer("laboratoire")
    station.ramasser("bonbonne")
    station.utiliser("bonbonne")

    assert station.joueur.oxygene() == 68
    assert station.joueur.possede("bonbonne") == False

    station.utiliser("bonbonne")

    assert station.joueur.oxygene() == 68


def test_oxygene_insuffisant():
    station = StationManager()

    station.deplacer("laboratoire")
    station.ramasser("bonbonne")
    station.joueur.consommer(38)

    assert station.joueur.oxygene() == 2

    station.utiliser("bonbonne")

    assert station.joueur.oxygene() == 0
    assert station.joueur.possede("bonbonne") == True
    assert station.terminee() == True


def test_victoire():
    station = StationManager()

    station.deplacer("réserve")
    station.ramasser("badge")
    station.ramasser("câble")
    station.deplacer("sas")
    station.deplacer("laboratoire")
    station.ramasser("fusible")
    station.ramasser("bonbonne")
    station.utiliser("bonbonne")
    station.journal()
    station.utiliser("badge")

    assert station.maintenance == True
    assert station.joueur.possede("badge") == True

    station.deplacer("machines")

    oxygene = station.joueur.oxygene()
    station.tenter_code("4729")

    assert station.reacteur == False
    assert station.joueur.oxygene() == oxygene

    station.utiliser("câble")
    station.utiliser("fusible")

    assert station.joueur.possede("câble") == False
    assert station.joueur.possede("fusible") == False

    station.tenter_code("1234")

    assert station.reacteur == False
    assert station.joueur.oxygene() == 34

    station.tenter_code("4729")

    assert station.reacteur == True

    station.deplacer("commande")
    station.evacuer()

    assert station.victoire == True
    assert station.terminee() == True
    assert station.joueur.oxygene() == 22


def test_defaite():
    station = StationManager()

    for i in range(10):
        station.attendre()

    assert station.joueur.oxygene() == 0
    assert station.victoire == False
    assert station.terminee() == True


if __name__ == "__main__":
    test_joueur()
    test_salle()
    test_enigmes()
    test_deplacement()
    test_inventaire()
    test_bonbonne()
    test_oxygene_insuffisant()
    test_victoire()
    test_defaite()

    print("Tous les tests sont réussis !")
