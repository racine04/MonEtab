from Etab2 import ajouter_utilisateur_defaut, create_connection, create_database_and_tables, verifier_utilisateur
from menus import menu_principal
from colorama import Fore, Style, init

# Initialise colorama
init(autoreset=True)

class main():

  print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")
  print(f"{Fore.LIGHTCYAN_EX}                          CONNEXION              ")
  print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")

  conn= create_connection()
  if conn :
    create_database_and_tables()
    ajouter_utilisateur_defaut(conn)
    pseudo = input("Entrez votre pseudo:")
    mot_passe = input("Entrez votre mot de passe:")
    if verifier_utilisateur(pseudo, mot_passe):
        menu_principal()
    else : 
        print(f"{Fore.LIGHTRED_EX} Connexion echoue")
    conn.close()
  else :
    print(f"{Fore.LIGHTRED_EX} Connexion a la base de donnees echoue")

if __name__ == "__main__":
   main()
          


      





              

        




    
