def generer_mdp(longueur):

    minuscules = string.ascii_lowercase
    majuscules = string.ascii_uppercase
    chiffres = string.digits
    speciaux = string.punctuation

    alphabet = (
        minuscules +
        majuscules +
        chiffres +
        speciaux
    )

    mot_de_passe = []

    mot_de_passe.append(random.choice(minuscules))
    mot_de_passe.append(random.choice(majuscules))
    mot_de_passe.append(random.choice(chiffres))
    mot_de_passe.append(random.choice(speciaux))
    print(mot_de_passe)

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

import time
import random
import string

generer_mdp(8)