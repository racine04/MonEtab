import datetime
from mysql.connector import Error
from colorama import Fore, Style, init

# Initialise colorama
init(autoreset=True)

def ajouter_eleve(conn):
    cursor = conn.cursor()

    # Récupérer les informations de l'élève depuis la console
    nom = input("Entrez le nom de l'élève: ")
    prenom = input("Entrez le prénom de l'élève: ")
    while True:
        date_naissance_str = input("Entrez date de naissance de l'eleve (format JJ-MM-AAAA): ")
        try:
            # Convertir la chaîne en un objet date
            date = datetime.datetime.strptime(date_naissance_str, "%d-%m-%Y").date()
            break  # Sortir de la boucle si la date est valide
        except ValueError:
            print(f"{Fore.LIGHTRED_EX} Format de date invalide. Veuillez entrer la date au format JJ-MM-AAAA.")
    ville= input("Entrez la ville de l'eleve:")
    telephone = input("Entrez le numero de telephone de l'eleve:")
    classe = input("Entrez la classe de l'eleve:")
    matricule = input("Entrez le matricule de l'élève: ")

    # Insertion des informations dans la base de données
    cursor.execute("INSERT INTO eleves (nom, prenom, date_naissance, ville, telephone, classe, matricule) VALUES (%s, %s, %s, %s, %s, %s, %s)", (nom, prenom, date, ville, telephone, classe, matricule))

    # Sauvegarde des modifications
    conn.commit()

    print(f"{Fore.LIGHTGREEN_EX} L'élève {nom} {prenom} a été ajouté avec succès.")

def modifier_eleve(conn):
    cursor = conn.cursor()
    matricule = input("Entrez le matricule de l'élève: ")

    cursor.execute("SELECT * FROM eleves WHERE matricule = %s", (matricule,))
    eleve = cursor.fetchone()

    if eleve:
        print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")
        print(f"{Fore.LIGHTCYAN_EX}                   INFORMATIONS SUR L'ELEVE              ")
        print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")
        print(f"Nom: {eleve[1]}")
        print(f"Prenom: {eleve[2]}")
        print(f"Date de naissance: {eleve[3]}")
        print(f"Ville: {eleve[4]}")
        print(f"Telephone: {eleve[5]}")
        print(f"Classe: {eleve[6]}")
        print(f"Matricule: {eleve[7]}")
        print("")
        print("********** QUE SOUHAITEZ-VOUS MODIFIER ? **********")
        print("")

        print("1. Modifier le nom")
        print("2. Modifier le prenom")
        print("3. Modifier la date de naissance")
        print("4. Modifier la ville")
        print("5. Modifier le numero de telephone")
        print("6. Modifier la classe")
        choix = int(input("Choisissez une option: "))

        if choix == 1:
            nom = input("Entrez le nouveau nom: ")
            cursor.execute("""
                UPDATE eleves
                SET nom = %s
                WHERE matricule = %s
            """, (nom, matricule))
            conn.commit()
            print(f"{Fore.LIGHTGREEN_EX} Le nom a été mis à jour avec succès.")
        # Ajoutez des conditions similaires pour les autres options de modification
        if choix == 2:
            prenom = input("Entrez le nouveau prenom: ")
            cursor.execute("""
            UPDATE eleves
            SET prenom = %s
            WHERE matricule = %s
             """, (prenom, matricule))
            conn.commit()
            print(f"{Fore.LIGHTGREEN_EX} Le prenom a été mis à jour avec succès.")
        if choix == 3:
            while True:
             date_naissance_str = input("Entrez la nouvelle date de naissance de l'eleve (format JJ-MM-AAAA): ")
             try:
            # Convertir la chaîne en un objet date
                date = datetime.datetime.strptime(date_naissance_str, "%d-%m-%Y").date()
                break  # Sortir de la boucle si la date est valide
             except ValueError:
              print(f"{Fore.LIGHTRED_EX} Format de date invalide. Veuillez entrer la date au format JJ-MM-AAAA.")
            cursor.execute("""
                 UPDATE eleves
                 SET date_naissance = %s
                 WHERE matricule = %s
             """, (date, matricule))
            conn.commit()
            print(f"{Fore.LIGHTGREEN_EX} La date de naissance a été mis à jour avec succès.")
        if choix == 4:
            ville = input("Entrez la nouvelle ville: ")
            cursor.execute("""
            UPDATE eleves
            SET ville = %s
            WHERE matricule = %s
             """, (ville, matricule))
            conn.commit()
            print(f"{Fore.LIGHTGREEN_EX} La ville a été mise à jour avec succès.")
        if choix == 5:
            telephone = input("Entrez le nouveau numero de telephone: ")
            cursor.execute("""
            UPDATE eleves
            SET telephone = %s
            WHERE matricule = %s
             """, (telephone, matricule))
            conn.commit()
            print(f"{Fore.LIGHTGREEN_EX} Le numero de telephone a été mis à jour avec succès.")
        if choix == 6:
            classe = input("Entrez la nouvelle classe: ")
            cursor.execute("""
            UPDATE eleves
            SET classe = %s
            WHERE matricule = %s
             """, (classe, matricule))
            conn.commit()
            print(f"{Fore.LIGHTGREEN_EX} La classe a été mise à jour avec succès.")             

    else:
        print(f"{Fore.LIGHTRED_EX} Aucun élève trouvé avec ce matricule.")

    cursor.close()

def lister_eleves(conn):
    cursor = conn.cursor()

    # Exécuter la requête pour récupérer tous les élèves
    cursor.execute("SELECT * FROM eleves")

    # Récupérer tous les résultats
    eleves = cursor.fetchall()

    if eleves:
        print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")
        print(f"{Fore.LIGHTCYAN_EX}                      LISTE DES ELEVES              ")
        print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")
        for eleve in eleves:
            print(f"ID: {eleve[0]}")
            print(f"Nom: {eleve[1]}")
            print(f"Prénom: {eleve[2]}")
            print(f"Date de naissance: {eleve[3]}")
            print(f"Ville: {eleve[4]}")
            print(f"Téléphone: {eleve[5]}")
            print(f"Classe: {eleve[6]}")
            print(f"Matricule: {eleve[7]}")
            print(f"{Fore.LIGHTCYAN_EX} -" * 30)  # Séparateur entre chaque élève
    else:
        print(f"{Fore.LIGHTRED_EX} Aucun élève trouvé dans la base de données.")

    cursor.close()


def supprimer_eleve(conn):
    cursor = conn.cursor()

    # Demander le matricule de l'élève à supprimer
    matricule = input("Entrez le matricule de l'élève à supprimer: ")

    # Exécuter la requête pour vérifier si l'élève existe
    cursor.execute("SELECT * FROM eleves WHERE matricule = %s", (matricule,))
    eleve = cursor.fetchone()

    if eleve:
        # Demander une confirmation avant de supprimer
        confirmation = input(f"{Fore.LIGHTCYAN_EX} Êtes-vous sûr de vouloir supprimer l'élève {eleve[1]} {eleve[2]} (O/N)? ").lower()
        if confirmation == 'o':
            # Exécuter la requête pour supprimer l'élève
            cursor.execute("DELETE FROM eleves WHERE matricule = %s", (matricule,))
            conn.commit()  # Appliquer les changements dans la base de données
            print(f"{Fore.LIGHTRED_EX} L'élève a été supprimé avec succès.")
        else:
            print("Opération annulée.")
    else:
        print(f"{Fore.LIGHTRED_EX} Aucun élève trouvé avec ce matricule.")

    cursor.close()
              