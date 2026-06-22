import string

mot_de_passe = input("quelle est votre mot de passe ?")

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