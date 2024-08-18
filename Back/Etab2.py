import mysql.connector
from mysql.connector import Error
from colorama import Fore, Style, init

# Initialise colorama
init(autoreset=True)


def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='etab_db'
        )
        return connection
    except Error as e:
        print(f"{Fore.LIGHTRED_EX} Erreur de connexion: {e}")
        return None



def create_database_and_tables():
    connection = create_connection()
    if connection:
        try:
            curseur = connection.cursor()
            curseur.execute("CREATE DATABASE IF NOT EXISTS etab_db;")
            curseur.execute("USE etab_db;")

            tables = [
                """
                CREATE TABLE IF NOT EXISTS utilisateurs (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    pseudo VARCHAR(50) NOT NULL UNIQUE,
                    mot_de_passe VARCHAR(255) NOT NULL,
                    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS eleves (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nom VARCHAR(50) NOT NULL,
                    prenom VARCHAR(50) NOT NULL,
                    date_naissance DATE NOT NULL,
                    ville VARCHAR(100) NOT NULL,
                    telephone VARCHAR(15) NOT NULL,
                    classe VARCHAR(50),
                    matricule VARCHAR(50) UNIQUE
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS professeurs (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nom VARCHAR(50) NOT NULL,
                    prenom VARCHAR(50) NOT NULL,
                    date_naissance DATE NOT NULL,
                    ville VARCHAR(100) NOT NULL,
                    telephone VARCHAR(15) NOT NULL,
                    vacant BOOLEAN,
                    matiere_enseigne VARCHAR(100),
                    prochain_cours VARCHAR(100),
                    sujet_prochaine_reunion VARCHAR(100)
                );
                """
            ]
            for table in tables:
                curseur.execute(table)
            print(f"{Fore.LIGHTGREEN_EX} Tables créées avec succès.")
        except Error as e:
            print(f"{Fore.LIGHTRED_EX} Erreur lors de la création des tables: {e}")
        finally:
            curseur.close()
            connection.close()


def ajouter_utilisateur_defaut(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM utilisateurs WHERE pseudo = 'admin'")
    admin_user= cursor.fetchone()
    if admin_user :
        print(f"{Fore.LIGHTCYAN_EX} Utilisateur existe deja")
    else :
        cursor.execute("INSERT INTO utilisateurs(pseudo, mot_de_passe) VALUES (%s, %s)", ('admin', 'admin'))
        connection.commit()
        print(f"{Fore.LIGHTGREEN_EX} Utilisateur cree avec succes")    

def verifier_utilisateur(pseudo, mot_de_passe):
    connection = create_connection()
    if connection:
        try:
            curseur = connection.cursor(dictionary=True)
            query = "SELECT * FROM utilisateurs WHERE pseudo = %s;"
            curseur.execute(query, (pseudo,))
            utilisateur = curseur.fetchone()

            if utilisateur:
                mot_de_passe_stocke = utilisateur['mot_de_passe']
                # Vérifier si le mot de passe correspond
                if mot_de_passe == mot_de_passe_stocke:
                    print(f"{Fore.LIGHTGREEN_EX} Connexion réussie.")
                    return True
                else:
                    print(f"{Fore.LIGHTRED_EX} Mot de passe incorrect.")
                    return False
            else:
                print(f"{Fore.LIGHTRED_EX} Pseudo incorrect.")
                return False

        except Error as e:
            print(f"{Fore.LIGHTRED_EX} Erreur lors de la vérification de l'utilisateur: {e}")
            return False
        finally:
            curseur.close()
            connection.close()
    else:
        print(f"{Fore.LIGHTRED_EX} Erreur de connexion à la base de données.")
        return False


