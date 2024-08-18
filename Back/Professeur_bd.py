import datetime
from mysql.connector import Error
from colorama import Fore, Style, init

# Initialise colorama
init(autoreset=True)

def ajouter_prof(conn):
    cursor = conn.cursor()

    # Récupérer les informations du professeur depuis la console
    nom = input("Entrez le nom du professeur: ")
    prenom = input("Entrez le prénom du professeur: ")
    while True:
        date_naissance_str = input("Entrez la date de naissance du professeur (format JJ-MM-AAAA): ")
        try:
            # Convertir la chaîne en un objet date
            date_naissance = datetime.datetime.strptime(date_naissance_str, "%d-%m-%Y").date()
            break  # Sortir de la boucle si la date est valide
        except ValueError:
            print(f"{Fore.LIGHTRED_EX} Format de date invalide. Veuillez entrer la date au format JJ-MM-AAAA.")
    
    ville = input("Entrez la ville du professeur: ")
    telephone = input("Entrez le numéro de téléphone du professeur: ")

    # Demander si le professeur est vacant
    while True:
        vacant_str = input("Le professeur est-il vacant ? (o/n): ").lower()
        if vacant_str == 'o':
            vacant = True
            break
        elif vacant_str == 'n':
            vacant = False
            break
        else:
            print("Veuillez entrer 'o' pour oui ou 'n' pour non.")
    
    matiere_enseigne = input("Entrez la matière enseignée par le professeur: ")
    prochain_cours = input("Entrez le prochain cours du professeur: ")
    sujet_prochaine_reunion = input("Entrez le sujet de la prochaine réunion: ")

    # Insertion des informations dans la base de données
    cursor.execute("""
        INSERT INTO professeurs (nom, prenom, date_naissance, ville, telephone, vacant, matiere_enseigne, prochain_cours, sujet_prochaine_reunion) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (nom, prenom, date_naissance, ville, telephone, vacant, matiere_enseigne, prochain_cours, sujet_prochaine_reunion))

    # Sauvegarde des modifications
    conn.commit()

    print(f"{Fore.LIGHTGREEN_EX} Le professeur {nom} {prenom} a été ajouté avec succès.")
    cursor.close()


def modifier_prof(conn):
    cursor = conn.cursor()
    nom = input("Entrez le nom du professeur: ")

    cursor.execute("SELECT * FROM professeurs WHERE nom = %s", (nom,))
    prof = cursor.fetchone()

    if prof:
        print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")
        print(f"{Fore.LIGHTCYAN_EX}                INFORMATIONS SUR LE PROFESSEUR              ")
        print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")
        print(f"Nom: {prof[1]}")
        print(f"Prenom: {prof[2]}")
        print(f"Date de naissance: {prof[3]}")
        print(f"Ville: {prof[4]}")
        print(f"Telephone: {prof[5]}")
        print(f"Vacant: {prof[6]}")
        print(f"Matiere enseigne: {prof[7]}")
        print(f"Prochain cours: {prof[8]}")
        print(f"Sujet de la prochaine reunion: {prof[9]}")
        print("")
        print("********** QUE SOUHAITEZ-VOUS MODIFIER ? **********")
        print("")
        print("1. Modifier le nom")
        print("2. Modifier le prenom")
        print("3. Modifier la date de naissance")
        print("4. Modifier la ville")
        print("5. Modifier le numero de telephone")
        print("6. Modifier le statut")
        print("6. Modifier la matiere enseigne")
        print("6. Modifier le prochain cours")
        print("6. Modifier le sujet de la prochaine reunion")
        choix = int(input(f"{Fore.LIGHTCYAN_EX} Choisissez une option: "))

        if choix == 1:
            nom = input("Entrez le nouveau nom: ")
            cursor.execute("""
                UPDATE professeurs
                SET nom = %s
                WHERE nom = %s
            """, (nom, nom))
            conn.commit()
            print(f"{Fore.LIGHTGREEN_EX} Le nom a été mis à jour avec succès.")
        # Ajoutez des conditions similaires pour les autres options de modification
        if choix == 2:
            prenom = input("Entrez le nouveau prenom: ")
            cursor.execute("""
            UPDATE professeurs
            SET prenom = %s
            WHERE nom = %s
             """, (prenom, nom))
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
                 UPDATE professeurs
                 SET date_naissance = %s
                 WHERE nom = %s
             """, (date, nom))
            conn.commit()
            print(f"{Fore.LIGHTGREEN_EX} La date de naissance a été mis à jour avec succès.")
        if choix == 4:
            ville = input("Entrez la nouvelle ville: ")
            cursor.execute("""
            UPDATE professeurs
            SET ville = %s
            WHERE nom = %s
             """, (ville, nom))
            conn.commit()
            print(f"{Fore.LIGHTGREEN_EX} La ville a été mise à jour avec succès.")
        if choix == 5:
            telephone = input("Entrez le nouveau numero de telephone: ")
            cursor.execute("""
            UPDATE professeurs
            SET telephone = %s
            WHERE nom = %s
             """, (telephone, nom))
            conn.commit()
            print(f"{Fore.LIGHTGREEN_EX} Le numero de telephone a été mis à jour avec succès.")
        if choix == 6:
            while True:
              vacant_str = input("Le professeur est-il vacant ? (o/n): ").lower()
              if vacant_str == 'o':
                 vacant = True
                 break
              elif vacant_str == 'n':
                 vacant = False
                 break
              else:
                print("Veuillez entrer 'o' pour oui ou 'n' pour non.")
            cursor.execute("""
            UPDATE professeurs
            SET vacant = %s
            WHERE nom = %s
             """, (vacant, nom))
            conn.commit()
            print(f"{Fore.LIGHTGREEN_EX} Le statut a été mise à jour avec succès.") 
        if choix == 7:
            matierEnseigne = input("Entrez la nouvelle matiere enseigne: ")
            cursor.execute("""
            UPDATE professeurs
            SET matiere_enseigne = %s
            WHERE nom = %s
             """, (matierEnseigne, nom))
            conn.commit()
            print(f"{Fore.LIGHTGREEN_EX} La matiere enseigne a été mise à jour avec succès.")
        if choix == 8:
            prochainCours = input("Entrez le prochain cours: ")
            cursor.execute("""
            UPDATE professeurs
            SET prochain_cours = %s
            WHERE nom = %s
             """, (prochainCours, nom))
            conn.commit()
            print(f"{Fore.LIGHTGREEN_EX} Le prochain cours a été mis à jour avec succès.")
        if choix == 9:
            prochaineReunion = input("Entrez le sujet de reunion: ")
            cursor.execute("""
            UPDATE professeurs
            SET sujet_prochaine_reunion = %s
            WHERE nom = %s
             """, (prochaineReunion, nom))
            conn.commit()
            print(f"{Fore.LIGHTGREEN_EX} Le sujet de la prochaine reunion a été mis à jour avec succès.")                        

    else:
        print(f"{Fore.LIGHTRED_EX} Aucun professeur trouvé avec ce nom.")

    cursor.close()

def lister_prof(conn):
    cursor = conn.cursor()

    # Exécuter la requête pour récupérer tous les élèves
    cursor.execute("SELECT * FROM professeurs")

    # Récupérer tous les résultats
    professeurs = cursor.fetchall()

    if professeurs:
        print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")
        print(f"{Fore.LIGHTCYAN_EX}                    LISTE DES PROFESSEURS              ")
        print(f"{Fore.LIGHTCYAN_EX}            *************************************               ")
        for professeur in professeurs:
            print(f"ID: {professeur[0]}")
            print(f"Nom: {professeur[1]}")
            print(f"Prénom: {professeur[2]}")
            print(f"Date de naissance: {professeur[3]}")
            print(f"Ville: {professeur[4]}")
            print(f"Téléphone: {professeur[5]}")
            print(f"Vacant: {professeur[6]}")
            print(f"Matiere: {professeur[7]}")
            print(f"Prochain cours: {professeur[8]}")
            print(f"Sujet prochaine reunion: {professeur[9]}")
            print(f"{Fore.LIGHTCYAN_EX} -" * 30)  # Séparateur entre chaque élève
    else:
        print(f"{Fore.LIGHTRED_EX} Aucun professeur trouvé dans la base de données.")

    cursor.close()


def supprimer_prof(conn):
    cursor = conn.cursor()

    # Demander le matricule de l'élève à supprimer
    nom = input("Entrez le nom du professeur à supprimer: ")

    # Exécuter la requête pour vérifier si l'élève existe
    cursor.execute("SELECT * FROM professeurs WHERE nom = %s", (nom,))
    professeur = cursor.fetchone()

    if professeur:
        # Demander une confirmation avant de supprimer
        confirmation = input(f"{Fore.LIGHTCYAN_EX} Êtes-vous sûr de vouloir supprimer le professeur {professeur[1]} {professeur[2]} (O/N)? ").lower()
        if confirmation == 'o':
            # Exécuter la requête pour supprimer l'élève
            cursor.execute("DELETE FROM professeurs WHERE nom = %s", (nom,))
            conn.commit()  # Appliquer les changements dans la base de données
            print(f"{Fore.LIGHTRED_EX} Le professeur a été supprimé avec succès.")
        else:
            print(f"{Fore.LIGHTCYAN_EX} Opération annulée.")
    else:
        print(f"{Fore.LIGHTRED_EX} Aucun professeur trouvé avec ce matricule.")

    cursor.close()

                