import random
import time
import string
import math

with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as f:
    leakedMDP = set(line.strip() for line in f)

# Création des fonctions de vérification

def contenu(mot_de_passe):
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
    else:
        print("✘ : Pas de majuscule")
    if minuscule:
        print("✔ : Contient une minuscule")
    else:
        print("✘ : Pas de minuscule")
    if chiffre:
        print("✔ : Contient un chiffre")
    else:
        print("✘ : Pas de chiffre")
    if special:
        print("✔ : Contient un caractère spécial")
    else:
        print("✘ : Pas de caractère spécial")

def repetition(mot_de_passe):
    alphabet=string.ascii_letters+string.digits+string.punctuation
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
    for i in range (len(alphabet)):
        if len(mot_de_passe)<=recherche(alphabet[i])*2.5:
            print("✘ : Le mot de passe contient trop de "+alphabet[i]+".")
        else:
            nonrepete=nonrepete+1
    if nonrepete==94:
        print("✔ : Le mot de passe ne contient pas de répétitions :)")

def rockyou_verif(mot_de_passe):
    if mot_de_passe in leakedMDP:
        print("✘ : Appartenance du mot de passe à rockyou.txt : OUI")
    else:
        print("✔ : Appartenance du mot de passe à rockyou.txt : NON")

def break_time(mot_de_passe):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    combinaisons = len(alphabet) ** len(mot_de_passe)
    vitesse = 1_000_000_000  # 1 milliard d'essais/s
    secondes = combinaisons / vitesse

    # Conversion
    annees = int(secondes // (365 * 24 * 3600))
    reste = secondes % (365 * 24 * 3600)
    jours = int(reste // (24 * 3600))
    reste %= (24 * 3600)
    heures = int(reste // 3600)

    print("Longueur :", len(mot_de_passe))
    print("Combinaisons :", f"{combinaisons:,}")

    print(
        f"Temps estimé : {annees:,} ans, "
        f"{jours} jours et "
        f"{heures} heures"
    )

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
        contenu(mot_de_passe)
        repetition(mot_de_passe)
        rockyou_verif(mot_de_passe)
        break_time(mot_de_passe)
        #if check_content+check_repet+check_rockyou==6:
        #    print("\n✔ : Le mot de passe est sécurisé.")
        #else:
        #    print("\n✘ : Le mot de passe n'est pas suffisamment sécurisé.\nVous pouvez en générer un sécurisé via le choix 2. dans le menu.")
        print("==== Fin du compte rendu ====")
        time.sleep(2)

    elif choix == "2":
        print("Choix 2")

    elif choix == "3":
        print("\nMerci d'avoir utilisé Pass Check'R, à bientôt!")
        time.sleep(1)
        break
    else:
        print("\nChoix invalide. Retour au menu.")