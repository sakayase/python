# exo 3.1
# Calculez la moyenne des nombres suivants : 1, 1, 2, 3, 5, 8, 13.
# Affectez le résultat à une variable et affichez le résultat.

# réponse 3.1
num_list = [1, 1, 2, 3, 5, 8, 13]
total = 0
for i in range(len(num_list)):
    total += num_list[i]
av_list = total / len(num_list)
print(av_list)


# exo 3.2
# On est en vacance et on veut suivre ses dépenses quotidiennes.
# Stockez le montant de chacune des dépenses quotidiennes dans une variable différente :
# - day1 : 26,82
# - day2 : 42,00
# - day3 : 31,41
# - day4 : 63,7
# - day5 : 32
# Stockez le nombre de jours dans une variable.
# Calculez le montant total des dépenses.
# Calculez la moyenne des dépenses quotidiennes en utilisant la variable contenant le nombre de jours et le total.
# Affichez le nombre jours, le montant total et la moyenne des dépenses.

# réponse 3.2

day1 = 26.82
day2 = 42.00
day3 = 31.41
day4 = 63.7
day5 = 32


num_days = 5

total_cost = day1 + day2 + day3 + day4 + day5
av_cost = total_cost / num_days

print(num_days, total_cost, av_cost)
# exo 3.3
# La formule suivante permet de convertir des mètres en miles :
# miles = meters / 1609.344
# Je dois marcher 2371 m pour aller jusqu'à la plu sproche boulangerie.
# Combien cela fait-il en miles ?
# Affichez un résultat arrondi

# réponse 3.3
distance = 2371
distance_miles = distance / 1609.344
print(round(distance_miles, 3))