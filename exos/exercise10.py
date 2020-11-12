# exercise-10.py

# exo 10.1
# Créer une fonction nommée `my_sum()` qui :
# - prend deux paramètres
# - additionne ces deux paramètres
# - renvoit le résultat
# Appelez la fonction et affichez le résultat

# réponse 10.1
def my_sum(a, b):
    return a + b

print(my_sum(10, 1))

# exo 10.2
# Créer une fonction nommée `my_diff()` qui :
# - prend deux paramètres de type `int`
# - soustrait ces deux paramètres
# - renvoit le résultat de type `int`
# Notez bien le type hinting dans la déclaration de la fonction
# Appelez la fonction et affichez le résultat

# réponse 10.2
def my_diff(a: int, b: int) -> int:
    return a - b

print(my_diff(10, 1))

# exo 10.3
# Créer une fonction nommée `oui_non()` qui :
# - prend un paramètre booléen
# - renvoit `oui` si le boolest est égal à True
# - renvoit `non` si le boolest est égal à False

# réponse 10.3
def oui_non(boolean: bool) -> str:
    if type(boolean) == bool and boolean:
        return "oui"
    else:
        return "non"

print(oui_non(True))
print(oui_non(False))
print(oui_non(1))

# exo 10.4
# Créer une fonction nommée `is_greater()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoit True si `a` est plus grand que `b`
# Appelez la fonction et affichez le résultat

# réponse 10.4
def is_greater(a: float, b: float) -> bool:
    if a > b:
        return True
    else:
        return False

print(is_greater(4, 8))
print(is_greater(8, 4))

# exo 10.5
# Créer une fonction nommée `compare()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoit 1 si `a` est plus grand que `b`
# - renvoit -1 si `a` est plus petit que `b`
# - renvoit 0 si `a` et `b` sont égaux
# Appelez la fonction et affichez le résultat

# réponse 10.5
def compare(a: float, b: float) -> int:
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

print(compare(4, 8))
print(compare(8, 4))
print(compare(4, 4))

# exo 10.6
# La formule suivante permet de converit des mètres en miles :
#
#       miles = meters / 1609.344
#
# La formule suivante permet de faire le contraire :
#
#       meters = miles * 1609.344
#
# Créez une fonction nommée :
#
# - metersToMiles() permettant de convertir des mètres en miles
# - milesToMeters() permettant de convertir des miles en mètres
#
# Ensuite convertissez les valeurs :
#
# - 100 mètres en miles
# - 100 miles en mètres
#
# Appelez les fonctions et affichez les résultats

# réponse 10.6
def metersToMiles(meters: float) -> float:
    return meters / 1609.344

def milesToMeters(miles: float) -> float:
    return miles * 1609.344

print(metersToMiles(100))
print(milesToMeters(100))

# exo 10.7
# Créer une fonction nommée `compute_tax()` qui :
# - prend un paramètre nommé `price` de type `float`
# - prend un paramètre nommé `tax_type` de type `int`
# - ajoute une taxe de 2,1 % à `price` si `tax_type` ets égal à `1`
# - ajoute une taxe de 5,5 % à `price` si `tax_type` ets égal à `2`
# - ajoute une taxe de 10 % à `price` si `tax_type` ets égal à `3`
# - ajoute une taxe de 20 % à `price` si `tax_type` ets égal à `4`
# Référence : [Quels sont les taux de TVA en vigueur en France et dans l'Union européenne ? | economie.gouv.fr](https://www.economie.gouv.fr/cedef/taux-tva-france-et-union-europeenne)
# Appelez la fonction et affichez le résultat avec un montant de 100 € pour chaque type de taxe

# réponse 10.7
def compute_tax(price: float, tax_type: int) -> float:
    if tax_type == 1:
        return price * 1.021
    elif tax_type == 2:
        return price * 1.055
    elif tax_type == 3:
        return price * 1.1
    elif tax_type == 4:
        return price * 1.2
    else:
        return (f"Type de taxe incorrect: {tax_type} n'est soit pas un entier, soit pas compris entre 1 et 4")

for i in range(1,6):
    print(f'100€ avec la taxe {i} : {compute_tax(100, i)}')