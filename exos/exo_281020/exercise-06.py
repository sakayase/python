# exercise-06.py

import random

# exo 6.1
# Créez une liste nommée `my_list` contenant un nombre entier, un nombre à virgule flottante, une chaîne de caractères et un booléen

# réponse 6.1
my_list = [3, 3.1415, "pi", True]

# exo 6.2
# Affichez l'élément qui se trouve à la troisième position de la liste
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.2
print(my_list[2])

# exo 6.3
# Ajoutez une chaîne de caractères à la liste `my_list` (sans modfier le code d'initialisation) et affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.3
my_list.append('test')
print(my_list)

# exo 6.4
# Supprimez l'élément qui se trouve en deuxièm position de la liste et affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.4
del(my_list[1])
print(my_list)

# exo 6.5
# Remplacez l'élément qui se trouve en deuxièm position de la liste par un nombre entier et affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.5
my_list[1] = 3
print(my_list)

# exo 6.6
# Affichez la taille de la liste
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.6
print(len(my_list))

# exo 6.7
# Inversez la position des valeurs `bar` et `lorem` puis affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.7
my_list[1], my_list[3] = my_list[3], my_list[1]
print(my_list)

# Remarque : les exercices suivants nécessitent l'utilisation d'une boucle `for`

# exo 6.8
# Calculez la somme des nombres de la liste et affichez le résultat
my_list = [2.71, 42]

# réponse 6.8
sum = 0 
for i in range(0, len(my_list)):
    sum += my_list[i]
print(sum)

sum = 0
for value in my_list:
    sum += value
print(sum)

# exo 6.9
# Calculez la somme des nombres de la liste et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.9
sum = 0
for value in my_list:
    sum += value
print(sum)

# exo 6.10
# Calculez la moyenne des nombres de la liste et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.10
sum = 0
for value in my_list:
    sum += value
print(sum / len(my_list))

# exo 6.11
# Trouvez l'index de la valeur `3.14` dans la liste et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.11
for value in my_list:
    if value == 3.14:
        print(value)
        break

# exo 6.12
# Comptez les nombres plus petits ou égaux à 10 dans la liste et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.12
count = 0
for value in my_list:
    if value <= 10:
        count += 1
print(count)

# exo 6.13
# Multipliez chacun des nombres dans la liste et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.13
count = 0
for value in my_list:
    my_list[count] = (value * 100)
    count += 1
print(my_list)

# exo 6.14
# Créez une deuxième liste ne contenant que les nombre entiers de la liste
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.14
my_list_int = []
for value in my_list:
    if type(value) is int:
        my_list_int.append(value)
print(my_list_int)

# exo 6.15
# Ici le but est d'intervertir les éléments de la liste deux à deux
# Liste initiale :
#
#   my_list = [2.71, 42, 123, 2, 3.14, 1.61]
#               0     1    2   3   4    5
# Résultat attendu :
#               0     1    2   3   4    5
#   my_list = [42, 2.71, 2, 123, 1.61, 3.14]
my_list = [2.71, 42, 123, 2, 3.14, 1.61, 2]

# réponse 6.15

for i in range(0, len(my_list)):
    if i % 2 == 0 and (i + 1 <= (len(my_list) - 1)):    #ON SE CASSE LA TETE POUR RIEN
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list) #inversé

# Ou

for i in range(0, len(my_list), 2):
    if i != len(my_list) - 1:                     
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list) #réinversé == a l'endroit
        

# exo 6.16
# Triez la liste en utilisant l'algorithme du tri bulle puis affichez la liste
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.16
count = 1
while count:
    count = 0
    for j in range(0, len(my_list) - 1):
        if my_list[j + 1] > my_list[j]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            count += 1 
print(my_list)

# tri_à_bulles(Tableau T)
#    pour i allant de (taille de T)-1 à 1
#        pour j allant de 0 à i-1
#            si T[j+1] < T[j]
#                échanger(T[j+1], T[j])


# code 6.1
# Lire la valeur de la ligne `m` et de la colonne `n` d'un tableau en 2 dimension
# print(matrix[m][n])
#
# Exemple avec la ligne 2 (index 1) et la colonne 3 (index 2)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
# Cette ligne affiche `6`
print(matrix[1][2])

# exo 6.17
# Affichez la valeur qui se trouve à la colonne 4, ligne 3
# Attention : il faut faire `- 1` pour obtenir les index correspondant
size = 5
matrix = []

for _ in range(0, size):
    row = [random.randint(40, 100) for _ in range(0, size)]
    matrix.append(row)

print(matrix)

# réponse 6.17
print(matrix[2][3])

# exo 6.18
# Avec le même tableau en 2 dimension, affichez toutes les valeurs plus petites ou égales à 50 ainsi que leur cordoonnées (ligne et colonne)

# réponse 6.18
for i in range(0, size): #size == len(matrix)
    for j in range(0, size): #size == len(matrix[i])
        if matrix[i][j] <= 50:
            print(f" ligne : {i + 1}, colonne : {j + 1}, valeur : {matrix[i][j]}")





