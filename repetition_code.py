motdepasse=input("Quel est votre mot de passe?")
alphabet=["a","b","c","d","e","f","g","h","i","j","k",
"l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
"1","2","3","4","5","6","7","8","9","0","@","!","#","$","%","^","&","*","-",
"_","+","=","?","<",">",".","A","B","C","D","E","F","G","H","I","J","K","L","M",
"N","O","P","Q","R","S","T","U","V","W","X","Y","Z","~","`",]
print(motdepasse)

def recherche(caractere):
    fois=0
    for c in motdepasse:
        if c==caractere:
            fois=fois+1
    return fois
if len(motdepasse)<7:
    print("Mot de passe non sécurisé")
else: 
    for i in range (len(alphabet)):
        if len(motdepasse)<=recherche(alphabet[i])*2.5:
            print("Trop de "+alphabet[i]+" dans le mot de passe.")
    
        