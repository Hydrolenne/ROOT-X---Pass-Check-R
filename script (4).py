import random
import string

# Chargement des mots de passe compromis
with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as fichier:
    mots_de_passe_compromis = set(ligne.strip() for ligne in fichier)

tous_les_caracteres = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

while True:
    mot_de_passe = ''.join(random.sample(tous_les_caracteres, 8))

    contient_majuscule = any(caractere.isupper() for caractere in mot_de_passe)
    contient_minuscule = any(caractere.islower() for caractere in mot_de_passe)
    contient_chiffre = any(caractere.isdigit() for caractere in mot_de_passe)
    contient_special = any(caractere in string.punctuation for caractere in mot_de_passe)

    if (contient_majuscule and contient_minuscule and
        contient_chiffre and contient_special and
        mot_de_passe not in mots_de_passe_compromis):
        break

print("Mot de passe généré :", mot_de_passe)

if mot_de_passe in mots_de_passe_compromis:
    print("Mot de passe compromis !")
else:
    print("Mot de passe OK")