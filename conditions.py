import random #importe la libraire ran
morning = True


#condition SI/SINON
if morning:                         #si : c'est le matin <=> si matin == True:
    print("c'est le matin")         
else:                               #sinon: 
    print("ce n'est pas le matin")

#ALT + FLECHE POUR DEPLACER UNE LIGNE/UN BLOC


product_quantity = random.randint(0, 5) #rand 0-100 : bornes comprises
print(product_quantity)

if product_quantity == 0:
    print("Rupture de stock")
elif product_quantity == 1:
    print("Il ne reste qu'un produit")
else:
    print(f"Il reste {product_quantity} produits") #f dans print pour {var} dans le string


electricity_off = True
water_off = True
# resultat : True

electricity_off = False
water_off = True
# resultat : False

electricity_off = True
water_off = False
# resultat : False

electricity_off = bool(random.randint(0,1))     #renvoie 0 ou 1 au hasard  
water_off = bool(random.randint(0,1))           # et est transformé par bool() en boolean 
                                            # si 0 alors faux si 1 alors vrai
# if electricity_off and water_off :
#     print("You're good to go")
# else:
#     print("You're not good to go")

print(water_off, electricity_off)

if electricity_off and water_off:
    print("You're good to go")
elif not electricity_off and water_off:
    print("You forgot to turn off the electricity")
elif electricity_off and not water_off:
    print("You forgot to turn of the water")
elif not electricity_off and not water_off:
    print("You forgot to turn of the water and electricity")
else:
    print("bug")


# TABLE DE VERITE DE L'OPERATEUR ET LOGIQUE

# A       B       A ET B
# True    True    True
# False   True    False
# True    False   False
# False   False   False

# -------------------

# TABLE DE VERITE DE L'OPERATEUR OU LOGIQUE

# A       B       A OU B
# True    True    True
# True    False   True
# False   True    True
# False   False   False

# -------------------

# TABLE DE VERITE DE L'OPERATEUR NOT

# A       not A
# True    False
# False   True

# -------------------

# TABLE DE VERITE DE L'OPERATEUR XOR

# A       B       A XOR B
# True    True    False
# False   True    True
# True    False   True
# False   False   False

# if (a == True) and (b == True): 
#     <=> 
# if (a == True) and \
#     (b == True):

