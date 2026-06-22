import random
import time

speciaux = "!@#$%&*?"

mdp = input("Entrez votre mot de passe : ")

majuscule = False
chiffre = False
special = False

for c in mdp:

    if c.isupper():
        majuscule = True

    if c.isdigit():
        chiffre = True

    if c in speciaux:
        special = True

print("\nAnalyse :")

if majuscule:
    print("✓ Majuscule détectée")

if chiffre:
    print("✓ Chiffre détecté")

if special:
    print("✓ Caractère spécial détecté")

print("\nAnalyse cryptographique...")

# Animation
for i in range(30):

    chaine = ""

    for j in range(25):
        chaine += random.choice(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "abcdefghijklmnopqrstuvwxyz"
            "0123456789"
            "!@#$%&*?"
        )

    print(chaine)
    time.sleep(0.05)

# Estimation
longueur = len(mdp)

if longueur < 6:
    duree = "quelques secondes"

elif longueur < 8:
    duree = "quelques minutes"

elif longueur < 10:
    duree = "quelques jours"

elif longueur < 12:
    duree = "plusieurs mois"

elif longueur < 14:
    duree = "plusieurs années"

else:
    duree = "des milliers d'années"

if majuscule and chiffre and special and longueur >= 12:
    duree = "des milliards d'années"

print("\n=== RESULTAT ===")
print("Longueur :", longueur)

if majuscule and chiffre and special:
    print("Mot de passe robuste")
else:
    print("Mot de passe faible")
print("Temps estimé pour le casser :", duree)