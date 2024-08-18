from datetime import date
import datetime
from colorama import Fore, Style, init

# Initialise colorama
init(autoreset=True)



def gestion_eleve():
    from gestion_eleves import gestion_eleve
    gestion_eleve()

def gestion_professeur():
    from gestion_professeur import gestion_professeurs
    gestion_professeurs()    

def gestion_utilisateur():
    from gestion_utilisateur import gestion_utilisateurs
    gestion_utilisateurs()

def menu_eleve() :
    print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")
    print(f"{Fore.LIGHTCYAN_EX}                     GESTION DES ELEVES              ")
    print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")
    print("")
    print(f"{Fore.LIGHTCYAN_EX} MENU")
    print("")
    print("   1: Ajouter un élève")
    print("   2: Supprimer un élève")
    print("   3: Modifier les informations de l'élève")
    print("   4: Lister les élèves")
    print("   5: Retour")
    print("   0: Accueil")
    print(f"{Fore.LIGHTCYAN_EX} Date systeme: ", date.today())

def menu_utilisateur() :
    print("")
    print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")
    print(f"{Fore.LIGHTCYAN_EX}                   GESTION DES UTILISATEURS              ")
    print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")
    print("")
    print("")
    print(f"{Fore.LIGHTCYAN_EX} MENU")
    print("")
    print("   1: Ajouter un utilisateur")
    print("   2: Supprimer un utilisateur")
    print("   3: Modifier les informations d'un utilisateur'")
    print("   4: Lister les utilisateurs")
    print("   5: Retour")
    print("   0: Accueil")
    print(f"{Fore.LIGHTCYAN_EX} Date systeme: ", date.today())    

def menu_professeurs() :
    print("")
    print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")
    print(f"{Fore.LIGHTCYAN_EX}                    GESTION DES PROFESSEURS              ")
    print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")
    print("")
    print("")
    print(f"{Fore.LIGHTCYAN_EX} MENU")
    print("")
    print("   1: Ajouter un professeur")
    print("   2: Supprimer un professeur")
    print("   3: Modifier les informations d'un professeur")
    print("   4: Lister les professeurs")
    print("   5: Retour")
    print("   0: Accueil")
    print(f"{Fore.LIGHTCYAN_EX} Date systeme: ", date.today())    


        

def quitter(startime): 
    endtime = datetime.now()
    duree = endtime - startime 
    print(f"{Fore.LIGHTCYAN_EX} \nAu revoir! Durée de la session : {duree}")


def menu_principal():
    print("")
    print(f"{Fore.LIGHTCYAN_EX} ******************************************************")
    print(f"{Fore.LIGHTCYAN_EX}         BIENVENU DANS L’APPLICATION ETAB v1.2")
    print(f"{Fore.LIGHTCYAN_EX} ******************************************************")
    print("")
    print(f"{Fore.LIGHTCYAN_EX} MENU:")
    print("")
    print("1: Gestion des élèves")
    print("2: Gestion des professeurs")
    print("3: Gestion des utilisateurs")
    print("0: Quitter")
    choix = input(f"{Fore.LIGHTCYAN_EX} Sélectionnez une option: ")

    if choix == "1":
        gestion_eleve()
    elif choix == "2":
        gestion_professeur()
    elif choix == "3":
        gestion_utilisateur()
    elif choix == "0":
        return
    else:
        print(f"{Fore.LIGHTRED_EX} Option invalide, veuillez réessayer.")
        