import datetime
from Eleve_bd import ajouter_eleve, lister_eleves, modifier_eleve, supprimer_eleve
from Etab2 import create_connection
from colorama import Fore, Style, init

# Initialise colorama
init(autoreset=True)

def gestion_eleve():
    conn= create_connection()
    eleves = []
    startime = datetime.datetime.now()
    
    while True: 
        from menus import menu_eleve, quitter
        menu_eleve()
        choix = input(f"{Fore.LIGHTCYAN_EX} Choisissez une option:")
        
        if int(choix) == 1:
            ajouter_eleve(conn)
        elif int(choix) == 2:
            supprimer_eleve(conn)
        elif int(choix) == 3:
            modifier_eleve(conn)
        elif int(choix) == 4:
            lister_eleves(conn)
        elif int(choix) == 5:
            quitter(startime)
            return
        else:
            print("Option invalide")
