import string

# Mot de passe saisi par l'utilisateur
mot_de_passe = input("Entrez un mot de passe : ")

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

# Affichage
print("\n----- Résultat -----")
print("Longueur :", len(mot_de_passe))

if combinaisons > 1_000_000_000:
    print("Combinaisons possibles : plus de 1 milliard de combinaisons")
else:
    print("Combinaisons possibles :", f"{combinaisons:,}".replace(",", " "))

if combinaisons / vitesse < 1:
    print("Temps de craquage estimé : inférieur à 1 seconde")
elif temps_en_annees > 1_000_000_000:
    print("Temps de craquage estimé : plus de 1 milliard d'années")
else:
    print(
        f"Temps de craquage estimé : "
        f"{annees:,} année(s), "
        f"{jours} jour(s), "
        f"{heures} heure(s), "
        f"{minutes} minute(s) et "
        f"{secondes} seconde(s)"
    )

    