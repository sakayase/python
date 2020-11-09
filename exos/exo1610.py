import random
# code 4.1
# la fonction random.randint() permet de tirer un nombre entier au hasard
# affectaction d'un nombre entier entre 0 et 99 à la variable number
# number = random.randint(0, 99)
# print(number)


# exo 4.1
# écrivez un bloc if qui affiche
# - "le nombre est égale à 1" si la variable number contient un 1
# - "le nombre est différent de 1" si la variable number ne contient pas de 1
# affectaction du nombre 0 ou 1 à la variable number
number = random.randint(0, 1)
print(number)

#reponse 4.1
boolnum = bool(number)  #0 = false 1 = true
if boolnum:
    print("le nombre est égal à 1")
else:
    print("le nombre est different de 1")

# code 4.2
# si 10 est un nombre pair, le modulo de 2 est égal à zéro
# print(10 % 2)
# si 21 est un nombre impair, le modulo de 2 ne sera pas égal à zéro (il sera égal à 1)
# print(21 % 2)
# exo 4.2
# écrivez un bloc if qui affiche
# - "le nombre est pair" si la variable number contient une valeur paire
# - "le nombre n'est pas pair, donc il est impair" si la variable number ne contient pas de valeur paire
# affectaction d'un nombre entier entre 0 et 9 à la variable number
number = random.randint(0, 9)
print(number)

#reponse 4.2
if not bool(number % 2):            #si le nombre est pair: bool -> false 
    print("le nombre est pair")     #et si il est impair : bool -> true
else:                               #donc not bool
    print("le nombre est impair")

# exo 4.3
# écrivez un bloc if qui affiche
# - "le nombre est supérieur ou égale à 5" si la variable number contient une valeur plus grande ou égale à 5
# - "le nombre est inférieur à 5" si la variable number ne contient pas de valeur plus grande ou égale à 5
# affectaction d'un nombre entier entre 0 et 9 à la variable number
number = random.randint(0, 9)
print(number)

#reponse 4.3
if number >= 5:
    print("le nombre est supérieur ou egal à 5")
else:
    print("le nombre est inférieur à 5")

# exo 4.4
# écrivez un bloc if qui affiche
# - "le nombre est compris entre 0 et 49 inclus" si la variable number contient une valeur comprise entre 0 et 49
# - "le nombre n'est pas compris entre 0 et 49 inclus" si la variable number ne contient pas de valeur comprise entre 0 et 49
# affectaction d'un nombre entier entre 0 et 99 à la variable number
number = random.randint(0, 99)
print(number)

#reponse 4.4
if number >= 49:
    print("le nombre est compris entre 0 et 49 inclus")
else:
    print("le nombre n'est pas compris entre 0 et 49 inclus")

# exo 4.5
# écrivez un bloc if qui affiche
# - "le nombre est compris entre 0 et 33 inclus" si la variable number contient une valeur comprise entre 0 et 33
# - "le nombre est compris entre 34 et 66 inclus" si la variable number contient une valeur comprise entre 34 et 66
# - "le nombre n'est pas compris entre 0 et 66 inclus" si la variable number ne contient pas de valeur comprise entre 0 et 66
# affectaction d'un nombre entier entre 0 et 99 à la variable number
number = random.randint(0, 99)
print(number)

#reponse 4.5
if number <= 33:
    print("le nombre est compris entre 0 et 33 inclus")
elif number >= 34 and number <= 66:
    print("le nombre est compris entre 34 et 66 inclus")
else:
    print("le nombre n'est pas compris entre 0 et 66 inclus")

# exo 4.6
# écrivez un bloc if qui affiche
# - "le nombre a est supérieur au nombre b" si la variable a contient une valeur plus grande que celle de la variable b
# - "le nombre b est supérieur au nombre a" si la variable b contient une valeur plus grande que celle de la variable a
# - "les deux nombre a et b sont égaux" si les deux variables a et b contiennent la même valeur
# affectaction d'un nombre entier entre 0 et 99 à la variable a
a = random.randint(0, 99)
print(a)
# affectaction d'un nombre entier entre 0 et 99 à la variable b
b = random.randint(0, 99)
print(b)

#reponse 4.6
if a > b:
    print("le nombre a est supérieur au nombre b")
elif b > a:
    print("le nombre b est supérieur au nombre a")
else: 
    print("les deux nombres a et b sont egaux")