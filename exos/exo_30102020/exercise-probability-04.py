import random
import time 

# Il existe un type de données particulier en Python : le tuple.

# code 4.1
my_tuple = ('foo', 123)

# Les tuples ressemblent aux listes car on peut y lire des données à la façon d'une liste.

# code 4.2
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1])

# Mais à la différence des listes, une fois que l'on a créé un tuple, on ne peut plus le changer.

# code 4.3
# Si vous activez le code suivante, vous verrez l'erreur "# TypeError: 'tuple' object does not support item assignment"
# my_tuple[0] = 'lorem'

# Cela ne vous empêche pas de changer complètement le contenu de la variable.
# Mais cela ne change rien au fait qu'on ne pas changer le tuple.

# code 4.4
my_tuple = None

# Malgré cette limitation, les tuples sont pratiques pour créer des objets composites à partir de données de base ("int", "float", "bool", "str")

# Par exemple, on peut s'en servir pour modéliser un jeu de carte à jouer.

# code 4.5
cards = []

for i in range(0, 4):
    # Dans un jeu, il y a les cartes de 1 à 10 et les têtes, dans 4 couleurs.
    # Pour les têtes : valet = 11, reine = 12 et roi = 13
    # Pour les couleurs : cœur = 0, carreau = 1, pique = 2, trèfle = 3
    for j in range(1, 14):
        if i == 0:
            color = 'rouge'
            symbol = 'cœur'
        elif i == 1:
            color = 'rouge'
            symbol = 'carreau'
        elif i == 2:
            color = 'noir'
            symbol = 'pique'
        elif i == 3:
            color = 'noir'
            symbol = 'trèfle'

        cards.append((symbol, color, j))

print(cards)

# Voici comment mélanger le jeu de carte.

# code 4.6
random.shuffle(cards)

# Voici comment tirer au hasard une carte du jeu.

# code 4.7
# sélection d'une carte au hasard
card = random.choice(cards)
print(card)
# suppression de la carte de la liste (la carte est dans les mains d'Alice)
cards.remove(card)

# Voici comment remettre une carte dans le jeu.

# code 4.8
cards.append(card)

# Voici comment tirer 1 carte du jeu, la mettre dans le paquet d'Alice et au final les remettre dans le jeu.

# code 4.9
# le paquet de carte d'Alice (au début, il est vide)
alice = []

# sélection d'une carte au hasard
card = random.choice(cards)
# suppression de la carte de la liste (la carte est dans les mains d'Alice)
cards.remove(card)
# ajout de la carte dans le paquet d'Alice
alice.append(card)

# remise des cartes d'alices dans le jeu
cards.extend(alice)
# suppression de toutes les carte d'Alices de son paquet
alice.clear()

# exo 4.1 : Rédigez le code qui affiche la valeur et la couleur de chaque carte du jeu.

# réponse 4.1
print("\n\n")
for card in cards: 
    print(f"Valeur de la carte : {card[2]}\nCouleur de la carte : {card[1]}")

# exo 4.2 : Alice tire 1 carte au hasard (sans la remettre dans le jeu).
# Puis Alice tire 1 carte au hasard (sans la remettre dans le jeu).
# Rédigez le code qui effectue ces opérations.
# Ensuite affichez le nombre de cartes qui restent dans le jeu et enfin remettez toutes les cartes dans le jeu.

# réponse 4.2
print("\n\n")
for i in range(0,2):
    card = random.choice(cards)
    cards.remove(card)
    alice.append(card)

print(f"Réponse 4.2: \nAlice a ces cartes : {alice} \nLe nombre de cartes restantes est : {len(cards)}")

# exo 4.3 : Bob tire 3 cartes au hasard (sans les remettre dans le jeu) et les met dans son paquet.
# Rédigez le code qui effectue ces opérations.
# Ensuite affichez le paquet de Bob, le nombre de cartes qui restent dans le jeu et remettez toutes les cartes dans le jeu.

# réponse 4.3
print("\n\n")
bob = []

for i in range(0,3):
    card = random.choice(cards)
    cards.remove(card)
    bob.append(card)

print(f"Réponse 4.3: \# Bob a ces cartes : {bob}\nLe nombre de cartes restantes est : {len(cards)}")


while bob or alice:
    if bob:
        card = bob[0]
        bob.remove(card)
        cards.append(card)
    if alice:
        card = alice[0]
        alice.remove(card)
        cards.append(card)

print(f"Il reste {len(cards)} cartes dans le jeu")
# exo 4.4 : Alice et Bob parient en jouant aux cartes.
# Voici comment se déroule le jeu :
# 1. Bob mélange les cartes, puis Alice tire trois cartes.
# 2. Elle parie que si un 3 (de n'importe quelle couleur) ou deux cœurs figurent parmi les cartes tirées, elle gagne.
# 3. Alice remets ses cartes dans le jeu, le mélange à nouveau, puis Bob tire 3 cartes.
# 4. Il parie que si un 7 (de n'importe quelle couleur) ou deux piques figurent parmi les cartes tirées, il gagne.
# 5. Bob remet ses cartes dans le jeu, ce qui termine une manche.
# Ils décident de faire trois manches.
# Rédigez le code qui modélise ce jeu et indiquez qui sera le gagnant des trois manches.

# réponse 4.4
print("\n\n")

wincount_alice = 0
wincount_bob = 0
win = False
while not win:
    random.shuffle(cards)

    for i in range(0,3):                    #Alice prend 3 cartes
        card = random.choice(cards)
        cards.remove(card)
        alice.append(card)

    count = 0
    card_win = []
    for card in alice:                      #Test pour savoir si elle a gagné
        if card[2] == 3:
            print(f"Alice gagne avec la carte {card}")
            wincount_alice += 1
        elif card[0] == 'cœur':
            count += 1
            card_win += card
            if count >= 2:
                wincount_alice += 1
                print(f"Alice gagne avec 2 coeurs : {card_win}")


    for i in range(0,len(alice)):           #On remet les cartes dans le jeu
        card = alice[0]
        alice.remove(card)
        cards.append(card)

    random.shuffle(cards)


    for i in range(0,3):                    #Bob prend 3 cartes
        card = random.choice(cards)
        cards.remove(card)
        bob.append(card)

    count = 0
    card_win = []
    for card in bob:                        #Test pour savoir si il a gagné 
        if card[2] == 7:
            print(f"Bob gagne avec la carte {card}")
            wincount_bob += 1
        elif card[0] == 'piques':
            count += 1
            card_win += card
            if count >= 2:
                print(f"Bob gagne avec 2 piques : {card_win}")
                wincount_bob += 1

    for i in range(0,len(bob)):           #On remet les cartes dans le jeu
        card = bob[0]
        bob.remove(card)
        cards.append(card)

    random.shuffle(cards)

    avance = 0                              #Test pour savoir si qqun a gagné
    if (wincount_alice == wincount_bob) and (wincount_alice >= 3 or wincount_bob >= 3):
        print(f"wincount alice : {wincount_alice} wincount bob: {wincount_bob}")
        print("Egalité, il faut une derniere manche pour départager")
    elif (wincount_alice == 3 and wincount_bob < 3):
        avance = wincount_alice - wincount_bob
        print(f"Alice gagne, avec {avance} manche(s) d'avance Bob")
        win = True
    elif (wincount_bob == 3 and wincount_alice < 3):
        avance = wincount_bob - wincount_alice
        print(f"Bob gagne, avec {avance} manche(s) d'avance sur Alice")
        win = True
    else: 
        print(f"wincount alice : {wincount_alice} wincount bob: {wincount_bob}")

    print(win)
    time.sleep(1)