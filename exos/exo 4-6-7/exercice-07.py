import random

# code 7.1
number = random.randint(1, 10)
# affectation d'un nombre aleatoire entre 1 et 10 inclus

# exo 7.1
# en utilisant une boucle for, affichez les nombre de 0 à 99 inclus
i = 0
for i in range(0, 100):
    print(i)


# exo 7.2
# en utilisant une boucle for, affichez les nombre de 0 à 100 inclus
i = 0
for i in range(0, 101):
    print(i)


# exo 7.3
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est égal à 1
i = 0
for i in range(0, 100):
    r = random.randint(1, 10)
    if r == 1:
        print(r)


# exo 7.4
# en utilisant une boucle for, on tire 50 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est plus petit ou égal à 5
i = 0
for i in range(0, 50):
    r = random.randint(1, 10)
    if r <= 5:
        print(r)


# exo 7.5
# en utilisant une boucle for, on tire 20 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est plus grand ou égal à 6
i = 0
for i in range(0, 20):
    r = random.randint(1, 10)
    if r >= 6:
        print(r)




# exo 7.6
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est égal à 1 ou égal à 10
i = 0
for i in range(0, 100):
    r = random.randint(1, 10)
    if r == 1:
        print(r)
    elif r == 10:
        print(r)




# exo 7.7
# en utilisant une boucle for, on tire 10 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est compris entre 3 et 8 inclus
i = 0
for i in range(0, 10):
    r = random.randint(1, 10)
    if r >= 3 and r <= 8:
        print(r)




# exo 7.8
# en utilisant une boucle for, on tire 50 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est égal à 7
# affichez la variable `count`
i = 0
count = 0
for i in range(0, 50):
    r = random.randint(1, 10)
    if r == 7:
        count += 1
print("le nombre de 7 est:",count)


# exo 7.9
# en utilisant une boucle for, on tire 10 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est plus petit ou égal à 4
# affichez la variable `count`
i = 0
count = 0
for i in range(0, 10):
    r = random.randint(1, 10)
    if r <= 4:
        count += 1
print("le nombre d'interation plus petit que 4 est:",count)



# exo 7.10
# en utilisant une boucle for, on tire 33 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est plus grand ou égal à 7
# affichez la variable `count`
i = 0
count = 0
for i in range(0, 33):
    r = random.randint(1, 10)
    if r >= 7:
        count += 1
print("le nombre d'interation plus grand que 7 est:",count)




# exo 7.11
# en utilisant une boucle for, on tire 66 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est plus petit ou égal à 2, ou plus grand ou égal à 9
# affichez la variable `count`
i = 0
count = 0
for i in range(0, 66):
    r = random.randint(1, 10)
    if r <= 2 or r >= 9:
        count += 1
print("le nombre d'iteration inférieure à 2 et supérieure à 9 est:",count)




# exo 7.12
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est compris entre 2 et 9 inclus
# affichez la variable `count`
i = 0
count = 0
for i in range(0, 66):
    r = random.randint(1, 10)
    if r >= 2 and r <= 9:
        count += 1
print("le nombre d'iteration entre 2 et 9 est:",count)



# exo 7.13
# en utilisant une boucle for, affichez tous les nombre pairs, de 1 à 99 inclus
i = 0
for i in range(0,100):
    if i % 2 == 0:
        print(i)



# exo 7.14
# en utilisant une boucle for, affichez tous les nombre pairs, de 1 à 100 inclus
i = 0
for i in range(0, 100):
    if i % 2 != 0:
        print(i)



# exo 7.15
# en utilisant une boucle for, affichez tous les nombres divisibles par 3, de 2 à 99 inclus
i = 0
for i in range(2, 100):
    if i % 3 == 0:
        print(i)



# code 7.16
# pour calculer la puissance 2 d'un nombre, on peut le multiplier par lui-même
number = 5
# print(number * number)
# mais on peut aussi l'élever à la puissance 2 avec l'opérateur puissance `**`
# print(number ** 2)
# exo 7.16
# en utilisant une boucle for, affichez la puissance 2 des nombres de 0 à 99 inclus
i = 0
for i in range(0, 100):
    print(f"{i} au carré =  {i ** 2}")


# code 7.3
# pour calculer la puissance 3 d'un nombre, on peut l'élever à la puissance 3 avec l'opérateur puissance `**`
number = 3
print(number ** 3)
# exo 7.17
# en utilisant une boucle for, affichez la puissance 3 des nombres de 1 à 100 inclus
i = 0
for i in range(0, 101):
    print(f"{i} puissance 3 =  {i ** 3}")



# exo 7.18
# dans une boucle while, on tire un nombre entier `r` au hasard entre 1 et 100 inclus
# boucler jusqu'à ce que la valeur 100 soit tirée au hasard

num_found = False
count = 0
while not num_found:
    num = random.randint(1, 100)
    count += 1
    if num == 100:
        print(f"Le nombre 100 à été trouvé apres {count} itérations")
        num_found = True
        


# trouver un chiffre ou un nombre dans une liste de nombres:
count = 0
for i in range (0, 100):
    str_i = str(i)
    if "1" in str_i:
        count += 1

print(count)