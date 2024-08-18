import datetime
from mysql.connector import Error
from colorama import Fore, Style, init

# Initialise colorama
init(autoreset=True)


def ajouter_utilisateur(conn):
    cursor = conn.cursor()

    # Récupérer les informations de l'élève depuis la console
    pseudo = input("Entrez votre pseudo: ")
    mot_de_passe = input("Entrez votre mot de passe: ")

    # Insertion des informations dans la base de données
    cursor.execute("INSERT INTO utilisateurs (pseudo, mot_de_passe) VALUES (%s, %s)", (pseudo, mot_de_passe))

    # Sauvegarde des modifications
    conn.commit()

    print(f"{Fore.LIGHTGREEN_EX} {pseudo} a été ajouté avec succès.")

def modifier_utilisateur(conn):
    cursor = conn.cursor()
    pseudo = input("Entrez votre pseudo: ")

    cursor.execute("SELECT * FROM utilisateurs WHERE pseudo = %s", (pseudo,))
    eleve = cursor.fetchone()

    if eleve:
        print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")
        print(f"{Fore.LIGHTCYAN_EX}                INFORMATIONS SUR L'UTILISATEUR              ")
        print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")
        print(f"Pseudo: {eleve[1]}")
        
        print(f"{Fore.LIGHTCYAN_EX} **********QUE SOUHAITEZ-VOUS MODIFIER ?**********")
        print("1. Modifier le pseudo")
        choix = int(input(f"{Fore.LIGHTCYAN_EX} Choisissez une option: "))

        if choix == 1:
            pseudo = input("Entrez le nouveau pseudo: ")
            cursor.execute("""
                UPDATE utilisateurs
                SET nom = %s
                WHERE pseudo = %s
            """, (pseudo, pseudo))
            conn.commit()
            print(f"{Fore.LIGHTGREEN_EX} Le pseudo a été mis à jour avec succès.")
        # Ajoutez des conditions similaires pour les autres options de modification
        

def lister_utilisateur(conn):
    cursor = conn.cursor()

    # Exécuter la requête pour récupérer tous les élèves
    cursor.execute("SELECT * FROM utilisateurs")

    # Récupérer tous les résultats
    utilisateurs = cursor.fetchall()

    if utilisateurs:
        print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")
        print(f"{Fore.LIGHTCYAN_EX}                    LISTE DES UTILISATEURS              ")
        print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")
        for utilisateur in utilisateurs:
            print(f"Pseudo: {utilisateur[1]}")

            
            print(f"{Fore.LIGHTCYAN_EX} -" * 30)  # Séparateur entre chaque élève
    else:
        print(f"{Fore.LIGHTRED_EX} Aucun utilisateur trouvé dans la base de données.")

    cursor.close()


def supprimer_utilisateur(conn):
    cursor = conn.cursor()

    # Demander le matricule de l'élève à supprimer
    pseudo = input("Entrez le matricule de l'utilisateur à supprimer: ")

    # Exécuter la requête pour vérifier si l'élève existe
    cursor.execute("SELECT * FROM utilisateurs WHERE pseudo = %s", (pseudo,))
    utilisateur = cursor.fetchone()

    if utilisateur:
        # Demander une confirmation avant de supprimer
        confirmation = input(f"{Fore.LIGHTCYAN_EX} Êtes-vous sûr de vouloir supprimer l'utilisateur {utilisateur[0]} (O/N)? ").lower()
        if confirmation == 'o':
            # Exécuter la requête pour supprimer l'élève
            cursor.execute("DELETE FROM utilisateurs WHERE pseudo = %s", (pseudo,))
            conn.commit()  # Appliquer les changements dans la base de données
            print(f"{Fore.LIGHTRED_EX} L'utilisateur a été supprimé avec succès.")
        else:
            print(f"{Fore.LIGHTCYAN_EX} Opération annulée.")
    else:
        print(f"{Fore.LIGHTRED_EX} Aucun utilisateur trouvé avec ce pseudo.")

    cursor.close()

                