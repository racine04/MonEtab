import datetime
from Etab2 import create_connection
from Professeur_bd import ajouter_prof, lister_prof, modifier_prof, supprimer_prof
from menus import menu_principal, menu_professeurs, quitter
from colorama import Fore, Style, init

# Initialise colorama
init(autoreset=True)

def gestion_professeurs():
    conn = create_connection()
    if not conn:
        print(f"{Fore.LIGHTRED_EX} Impossible de se connecter à la base de données.")
        return

    while True:
        menu_professeurs()  # Assurez-vous que cette fonction est correctement définie et importée
        choix_professeurs = input(f"{Fore.LIGHTCYAN_EX} Choisissez une option: ")
        
        if choix_professeurs == "1":
            ajouter_prof(conn)  # Assurez-vous que `ajouter_prof` est correctement défini et importé
        elif choix_professeurs == "2":
            supprimer_prof(conn)  # Assurez-vous que cette fonction est correctement définie et importée
        elif choix_professeurs == "3":
            modifier_prof(conn)  # Assurez-vous que cette fonction est correctement définie et importée
        elif choix_professeurs == "4":
            lister_prof(conn)  # Assurez-vous que cette fonction est correctement définie et importée
        elif choix_professeurs == "5":
            # Si vous avez une fonction de quitter, assurez-vous qu'elle est bien définie
            quitter(datetime.now())
            return
        elif choix_professeurs == "0":
            menu_principal()  # Assurez-vous que cette fonction est bien définie et accessible
        else:
            print(f"{Fore.LIGHTRED_EX} Option invalide. Veuillez réessayer.")
