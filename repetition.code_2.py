import string
motdepasse=input("Quel est votre mot de passe?")
alphabet=string.ascii_letters+string.digits+string.punctuation
liste=[alphabet.split()]
def recherche(caractere):
    fois=0
    for c in motdepasse:
        if c==caractere:
            fois=fois+1
    return fois
if len(motdepasse)<7:
    print("Mot de passe trop court")
else: 
    for i in range (len(alphabet)):
        if len(motdepasse)<=recherche(alphabet[i])*2.5:
            print("Trop de "+alphabet[i]+" dans le mot de passe.")
    
        