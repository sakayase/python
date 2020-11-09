# /!\ code style et nom de variable (anglais et explicite)

# 1 stocker le nombre de stagiaires dans une variable (int)
# 2 estimer une moyenne d'age (float)
# 3 nom et prenom dans une variable (str) 1 VARIABLE SEULEMENT
# 4 es t on au matin (bool)

nb_of_trainee = 20 # 1



#2
ages_of_trainees = [22, 25, 28, 31, 20, 18, 34, 38, 45, 21, 22, 25, 28, 30, 20, 18, 34, 38, 45, 21]
add_age = 0     #init du total de l'age
i = 0           #init du compteur
for i in ages_of_trainees:
    add_age += i
print(add_age)
average_age = add_age / nb_of_trainee
print("l'age moyen est :", average_age)


identity = "Simon Ponitzki" # 3
is_morning = False # 4


# exo 2.1  TRANSTYPAGE
# Stockez le valeurs suivantes dans une variable et transformez-les :
# 1- integer 2 en un float
# 2- float 1,62 en un integer
# 3- float 1,62 en un float arrondi
# puis faites un print de ces variables


integer1 = 2
integer1 = float(integer1)
print(type(integer1))
print(integer1)             #1

float1 = 1.62
float1 = int(float1)
print(type(float1))
print(float1)               #2

float1 = 1.62
float1 = round(float1)
print(type(float1)) 
print(float1)               #3


# Dans 5 variables qui correspondent chacune à des jours,
# stockez le montant des dépenses quotidiennes :
#  j1 : 26,82
#  j2 : 42,00
#  j3 : 31,41
#  j4 : 63,7
#  j5 : 32
# A partir de ces données, stockez dans 2 variables différentes :
#  le montant total des dépenses
#  la moyenne des dépenses quotidiennes
# Enfin, affichez les variables contenant le total et la moyenne avec la fonction print()



j1 = 26.82
j2 = 42.00
j3 = 31.41
j4 = 63.7
j5 = 32

total_cost = j1 + j2 + j3 + j4 + j5
daily_cost = total_cost / 5

print("le cout total est :", total_cost)
print("le cout journalier moyen est :", daily_cost)


print(round(1/3, 2)) #le chiffre apres la virgule = nb de chiffre apres la virgule