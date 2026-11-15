from station import StationManager

def main():
    print("===================================")
    print("MISSION ORION-7 : projet à réaliser")
    print("===================================")
    print("Bienvenue dans la station spatiale ORION-7")
    print("Votre objectif est de réparer le réacteur et de vous évacuer.")
    station = StationManager()

    while not station.terminee():
        print("\n================================")
        print(station.etat)
        print("================================")
        print("1. Observer la salle")
        print("2. Afficher l'inventaire")
        print("3. Se déplacer")
        print("4. Ramasser un objet")
        print("5. Utiliser un objet")
        print("6. Lire le journal")
        print("7. Saisir le code")
        print("8. Attendre")
        print("9. Évacuer")
        print("10. Afficher l'aide")

        choix = input("\nVotre choix : ")

        if choix == "1":
            print(station.observer())

        elif choix == "2":
            inventaire = station.joueur.inventaire()
            if not inventaire:
                print("Inventaire vide")
            else:
                print("Inventaire :", ", ".join(inventaire))

        elif choix == "3":
            destination = input("Destination : ").strip().lower()
            print(station.deplacer(destination))

        elif choix == "4":
            objet = input("Objet à ramasser : ").strip().lower()
            print(station.ramasser(objet))

        elif choix == "5":
            objet = input("Objet à utiliser : ").strip().lower()
            print(station.utiliser(objet))

        elif choix == "6":
            print(station.journal())

        elif choix == "7":
            code = input("Saisissez le code : ").strip()
            print(station.tenter_code(code))

        elif choix == "8":
            print(station.attendre())

        elif choix == "9":
            print(station.evacuer())

        elif choix == "10":
            print("Votre objectif est de réparer le réacteur.")
            print("Récupérez le badge, le câble et le fusible.")
            print("Surveillez votre niveau d'oxygène.")
            print("Déplacement : 6 oxygène")
            print("Observation : 1 oxygène")
            print("Ramassage : 2 oxygène")
            print("Utilisation : 2 oxygène")
            print("Lecture du journal : 1 oxygène")
            print("Tentative de code : 3 oxygène")
            print("Attente : 5 oxygène")
            print("Évacuation : 3 oxygène")

        else:
            print("Choix invalide.")

    print("\n================================")

    if station.victoire:
        print("VICTOIRE ! Vous avez quitté la station.")
    else:
        print("DÉFAITE ! Vous n'avez plus d'oxygène.")

    print("Oxygène restant :", station.joueur.oxygene())
    print("FIN DE LA PARTIE")
    print("================================")


if __name__ == "__main__":
    main()

    