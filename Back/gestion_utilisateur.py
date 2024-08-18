from Etab2 import create_connection
from Utilisateur_bd import ajouter_utilisateur, lister_utilisateur, modifier_utilisateur, supprimer_utilisateur
from menus import menu_principal, menu_utilisateur
from colorama import Fore, Style, init

# Initialise colorama
init(autoreset=True)

def gestion_utilisateurs():
    conn = create_connection()
    if not conn:
        print(f"{Fore.LIGHTRED_EX} Impossible de se connecter à la base de données.")
        return

    while True:
        menu_utilisateur()
        choix = input(f"{Fore.LIGHTCYAN_EX} Choisissez une option: ")
        
        if choix == "1":
            ajouter_utilisateur(conn)
        elif choix == "2":
            supprimer_utilisateur(conn)
        elif choix == "3":
            modifier_utilisateur(conn)
        elif choix == "4":
            lister_utilisateur(conn)
        elif choix == "5":
            break  # Retour au menu principal
        elif choix == "0":
            menu_principal()  # Retour au menu principal
        else:
            print(f"{Fore.LIGHTRED_EX} Option invalide. Veuillez réessayer.")