import math

mot_de_passe = input("entre mot de pass")

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

print("\nAnalyse du mot de passe :")

if len(mot_de_passe) >= 8:
    print(" Au moins 8 caractères")
else:
    print(" Moins de 8 caractères")

if majuscule:
    print(" Contient une majuscule")
else:
    print(" Pas de majuscule")

if minuscule:
    print(" Contient une minuscule")
else:
    print(" Pas de minuscule")

if chiffre:
    print(" Contient un chiffre")
else:
    print(" Pas de chiffre")

if special:
    print(" Contient un caractère spécial")
else:
    print(" Pas de caractère spécial")

if len(mot_de_passe) >= 8 and majuscule and minuscule and chiffre and special:
    print("\nMot de passe considéré comme fort.")
else:
    print("\nMot de passe à améliorer.")
    