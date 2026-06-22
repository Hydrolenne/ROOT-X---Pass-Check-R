with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as f:
    LeakedMDP = set(line.strip() for line in f)

MotDePasse = input("Mot de passe : ")

if MotDePasse in LeakedMDP:
    print("Mot de passe compromis !")
else:
    print("Mot de passe OK")