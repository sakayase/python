# Chargement du module random (pour générer des nombres aléatoires).
import random

# L'appel à la fonction random.randint(0, 1) renvoit un nombre entier aléatoire compris entre 0 et 1 inclus.
number = random.randint(0, 1)

# Pour savoir si la variable "number" vaut 1, je peux utiliser un bloc conditionnel.

# code 1.1
if number == 0:
    print("le nombre vaut 0")

# Pour savoir quel nombre la variable "number" vaut, je peux utiliser une boucle.

# code 1.2
for i in range(0, 2):
    if number == i:
        # affichage avec interpolation de la variable au moyen d'une "f-string"
        print(f"le nombre vaut {number}")

# exo 1.1 : Alice et Bob veulent jouer à pile ou face.
# - si la variable "head_or_tail" vaut 0, cela équivaut à pile
# - si elle vaut 1, cela équivaut à face
# Alice parie pile et Bob parie face.
# Qui gagne ? Alice ou Bob ?
# Rédigez le code qui indique le nom du gagnant.

# réponse 1.1
head_or_tail = random.randint(0 ,1)
if head_or_tail:
    print("bob wins")
else: 
    print("alice wins")

# exo 1.2 : Alice et Bob veulent jouer aux dés.
# Alice parie qu'elle va faire au moins 4. Bob parie qu'il va faire 3 au plus.
# Qui gagne ? Alice ou Bob ?
# Rédigez le code qui indique le nom du gagnant.

# réponse 1.2
dice = random.randint(1, 6)
if dice >= 4:
    print(f"le dé indique {dice}, c'est supérieur ou égal à 4 : alice wins")
else: 
    print(f"le dé indique {dice}, c'est inférieur ou egal à 3 : bob wins")


# exo 1.3 : Alice et Bob jouent à pierre papier ciseaux.
# - 1 équivaut à pierre
# - 2 équivaut à papier
# - 3 équivaut à ciseaux
# Rédigez le code qui indique qui gagne.

# réponse 1.3
pfc_bob = random.randint(1, 3)
pfc_alice = random.randint(1, 3)

if pfc_bob == pfc_alice:
    print("draw")
elif (pfc_bob == 1 and pfc_alice == 2) or (pfc_bob == 2 and pfc_alice == 3) or (pfc_bob == 3 and pfc_alice == 1):
    if pfc_bob == 1:
        print("bob a fait pierre")
    elif pfc_bob == 2:
        print("bob a fait papier")
    else:
        print("bob a fait ciseaux")
    
    if pfc_alice == 1:
        print("alice a fait pierre")
    elif pfc_alice == 2:
        print("alice a fait papier")
    else:
        print("alice a fait ciseaux")
    print("alice wins")
else:
    if pfc_bob == 1:
        print("bob a fait pierre")
    elif pfc_bob == 2:
        print("bob a fait papier")
    else:
        print("bob a fait ciseaux")
    
    if pfc_alice == 1:
        print("alice a fait pierre")
    elif pfc_alice == 2:
        print("alice a fait papier")
    else:
        print("alice a fait ciseaux")
    print("bob wins")