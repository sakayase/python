my_number1 = 123
my_number2 = 1.12
my_text = "bla bla bla"
my_boolean1 = True
my_boolean2 = False
my_null_value = None


# print(my_boolean1)
# print(my_boolean2)
# print(my_number1)
# print(my_number2)
# print(my_null_value)
# print(my_text)  

my_text3 = "test \n test"
        # \n = retour a la ligne

# print(my_text3)

# my_text4 = "erreure "de" syntaxe"

# print (my_text4)

my_text4_valide = "erreure \"de\" syntaxe"
# pour afficher un backslash -> \\ (le doubler)
# pour afficher un \n -> \\n
# pour afficher des guillemets utiliser les autres, ex : 'test "entre guillemets" test'
# affichera test "entre guillemets" test
print(my_text4_valide)

my_text5 = """une 
deux ''
trois"" lignes"""
# """ pour un retour à la ligne qd retour a la ligne sur le str
# + cela affiche les " et '
print(my_text5)


print("le type de variable de my_text5 est :" , type(my_text5))

my_number3 = int(my_number2)
print(my_number2, " devient ", my_number3) #transtypage d'un float en int

my_textfloat = "123.45"
my_number4 = float(my_textfloat) #transtypage en float d'un str
print(my_textfloat, "(str) devient ", my_number4, " (float)")

my_boolean3 = bool(my_textfloat) #transtypage en float d'un str
print(my_textfloat, "(str) devient ", my_boolean3, " (bool)")


a = 123
b = 456
print("a =", a)
print("b =", b)

# tmp = a
# a = b
# b = tmp

# OU
# uniquement en python

 a, b = b, a

print("a =", a)
print("b =", b)

