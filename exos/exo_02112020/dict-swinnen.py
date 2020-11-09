#exo 10.45 livre gérard swinnen apprendre python 3.5 (page 179 pdf 159 livre)

annuaire = {}


def add(dictionnaire, itt = 1):
    """ajoute une entrée au dictionnaire : (nom: (age, taille))
    possibillité d'itterer plusieurs fois l'ajout"""
    i = 0
    while i < itt:
        nom = ''
        age = 0
        taille = 0.0
        nom = str(input("Le nom du copain : "))
        age = int(input("L'age du copain : "))
        taille = float(input("La taille du copain : "))
        dictionnaire[nom] = (age, taille)
        i += 1
        

add(annuaire, 3)
print(annuaire)

def consult(dictionnaire, itt = 1):
    """lis le dictionnaire selon l'input de l'utilisateur
    posibilité d'itterer plusieurs fois"""
    i = 0
    while i < itt:
        nom = str(input("Le nom du copain : "))
        print(f"Nom : {nom} \nAge : {dictionnaire[nom][0]} ans \nTaille : {dictionnaire[nom][1]}m")
        i += 1

consult(annuaire)



