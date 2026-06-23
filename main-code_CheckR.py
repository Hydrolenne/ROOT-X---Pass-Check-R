import random
import time
import string
import math

with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as f:
    leakedMDP = set(line.strip() for line in f)

minuscules = string.ascii_lowercase
majuscules = string.ascii_uppercase
chiffres = string.digits
speciaux = string.punctuation
alphabet = (minuscules+majuscules+chiffres+speciaux)

# Création des fonctions de vérification

check=0

def contenu(mot_de_passe):
    global check
    majuscule = False
    minuscule = False
    chiffre = False
    special = False
    for caractere in mot_de_passe:
        if caractere.isupper():
            majuscule = True
        elif caractere.islower():
            minuscule = True
        elif caractere.isdigit():
            chiffre = True
        else:
            special = True

    if majuscule:
        print("✔ : Contient une majuscule")
        check=check+1
    else:
        print("✘ : Pas de majuscule")
    if minuscule:
        print("✔ : Contient une minuscule")
        check=check+1
    else:
        print("✘ : Pas de minuscule")
    if chiffre:
        print("✔ : Contient un chiffre")
        check=check+1
    else:
        print("✘ : Pas de chiffre")
    if special:
        print("✔ : Contient un caractère spécial")
        check=check+1
    else:
        print("✘ : Pas de caractère spécial")

def repetition(mot_de_passe):
    alphabet=string.ascii_letters+string.digits+string.punctuation
    global check
    nonrepete=0
    def recherche(caractere):
        fois=0
        for c in mot_de_passe:
            if c==caractere:
                fois=fois+1
        return fois
    if len(mot_de_passe)<7:
        print("✘ : Mot de passe trop court (inférieur à 7 caractères)")
    else: 
        print("✔ : Mot de passe assez long (suppérieur ou égal à 7 caractères)")
        check=check+1
    for i in range (len(alphabet)):
        if len(mot_de_passe)<=recherche(alphabet[i])*2.5:
            print("✘ : Le mot de passe contient trop de "+alphabet[i]+".")
        else:
            nonrepete=nonrepete+1
    if nonrepete==94:
        print("✔ : Le mot de passe ne contient pas de répétitions :)")
        check=check+1

def rockyou_verif(mot_de_passe):
    global check
    if mot_de_passe in leakedMDP:
        print("✘ : Appartenance du mot de passe à rockyou.txt : OUI")
    else:
        print("✔ : Appartenance du mot de passe à rockyou.txt : NON")
        check=check+1

def break_time(mot_de_passe):
    # Nombre de caractères possibles
    alphabet = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )
    # Calcul des combinaisons possibles
    combinaisons = len(alphabet) ** len(mot_de_passe)
    # Vitesse de test (exemple : 100 milliards de tentatives/seconde)
    vitesse = 100_000_000_000
    # Temps estimé en secondes
    temps = combinaisons / vitesse
    # Sauvegarde du temps total en années pour les tests
    temps_en_annees = temps / (365 * 24 * 3600)
    # Conversion en années, jours, heures, minutes, secondes
    annees = int(temps // (365 * 24 * 3600))
    temps %= (365 * 24 * 3600)
    jours = int(temps // (24 * 3600))
    temps %= (24 * 3600)
    heures = int(temps // 3600)
    temps %= 3600
    minutes = int(temps // 60)
    secondes = int(temps % 60)
    print("\n-> Nombre de caractères :", len(mot_de_passe))
    if combinaisons > 1_000_000_000:
        print("-> Combinaisons possibles : plus de 1 milliard de combinaisons")
    else:
        print("-> Combinaisons possibles :", f"{combinaisons:,}".replace(",", " "))
    if combinaisons / vitesse < 1:
        print("-> Temps de craquage estimé : inférieur à 1 seconde")
    elif temps_en_annees > 1_000_000_000:
        print("-> Temps de craquage estimé : plus de 1 milliard d'années")
    else:
        print(
            f"Temps de craquage estimé : "
            f"{annees:,} année(s), "
            f"{jours} jour(s), "
            f"{heures} heure(s), "
            f"{minutes} minute(s) et "
            f"{secondes} seconde(s)"
        )

def generer_mdp(longueur):
    minuscules = string.ascii_lowercase
    majuscules = string.ascii_uppercase
    chiffres = string.digits
    speciaux = string.punctuation

    alphabet = (minuscules+majuscules+chiffres+speciaux)
    mot_de_passe = []

    mot_de_passe.append(random.choice(minuscules))
    mot_de_passe.append(random.choice(majuscules))
    mot_de_passe.append(random.choice(chiffres))
    mot_de_passe.append(random.choice(speciaux))

    while len(mot_de_passe) < longueur:
        caractere = random.choice(alphabet)
        if caractere not in mot_de_passe:
            mot_de_passe.append(caractere)
        pass
    random.shuffle(mot_de_passe)

    mot_de_passe = "".join(mot_de_passe)
    if mot_de_passe in leakedMDP:
        return generer_mdp(longueur)
    return mot_de_passe


# Menu principal -----------------------------------------
print("\n\nBienvenue sur Pass Check'R by Root X!")
while True:
    print("\n===== PASS Check'R =====")
    print("1. Vérifier la solidité d'un mot de passe")
    print("2. Générer un mot de passe plus sécurisé")
    print("3. Quitter Pass Check'R")
    choix = input("Votre choix: ")

    if choix == "1":
        mot_de_passe = input("\n-> Saisissez le mot de passe que vous souhaitez vérifier : ")
        print("\n\n==== Compte rendu pour le mot de passe :", mot_de_passe,"====")
        check=0
        contenu(mot_de_passe)
        repetition(mot_de_passe)
        rockyou_verif(mot_de_passe)
        break_time(mot_de_passe)
        print("Note globale du mot de passe :",check,"/ 7")
        if check==7:
            print("\n✔ : Le mot de passe est sécurisé.")
        elif check==6:
            print("\n~ : Le mot de passe n'est pas le plus sécurisé, il peut être amélioré.")
        else:
            print("\n✘ : Le mot de passe n'est pas suffisamment sécurisé.\nVous pouvez en générer un sécurisé via le choix 2. dans le menu.")
        print("==== Fin du compte rendu ====")
        time.sleep(2)

    elif choix == "2":
        while True:
            try:
                longueur=int(input("\nLongueur du mot de passe à générer : "))
                if longueur<8:
                    print("La longueur doit être supérieure ou égale à 8.")
                    continue
                elif longueur > len(alphabet):
                    print("Longueur trop grande.")
                    continue
                break
            except ValueError:
                print("Veuillez entrer un nombre valide.")
        mot_de_passe=generer_mdp(longueur)
        print("\nMot de passe généré :", mot_de_passe)
        test=input("Souhaitez-vous tester le nouveau mot de passe ? (Yes/No) ")
        if test=="Yes" or test=="yes":
            print("\n\n==== Compte rendu pour le mot de passe :", mot_de_passe,"====")
            check=0
            contenu(mot_de_passe)
            repetition(mot_de_passe)
            rockyou_verif(mot_de_passe)
            break_time(mot_de_passe)
            print("Note globale du mot de passe :",check,"/ 7")
            if check==7:
                print("\n✔ : Le mot de passe est sécurisé.")
            elif check==6:
                print("\n~ : Le mot de passe n'est pas le plus sécurisé, il peut être amélioré.")
            else:
                print("\n✘ : Le mot de passe n'est pas suffisamment sécurisé.\nVous pouvez en générer un sécurisé via le choix 2. dans le menu.")
            print("==== Fin du compte rendu ====")
            time.sleep(2)
        else:
            print("Retour au menu.")
            time.sleep(1)

    elif choix == "3":
        print("\nMerci d'avoir utilisé Pass Check'R, à bientôt!")
        time.sleep(1)
        break
    else:
        print("\nChoix invalide. Retour au menu.")