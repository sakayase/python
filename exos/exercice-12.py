# exo 12.1
# Créez une classe nommée `User` qui possède les attributs suivants :
# - firstname: valeur par défaut ''
# - lastname: valeur par défaut ''
# - email: valeur par défaut ''
# - newsletter: valeur par défaut False
# et la méthode suivante :
# - __init__() : le constructeur
# Ne créez pas de getters et de setters

# réponse 12.1
class User:
    def __init__(self):
        '''contructeur de la classe User'''
        self._firstname: ''
        self._lastname: ''
        self._email: ''
        self._newsletter: False
        

# exo 12.2
# Créez 4 instances de la classe `User` et affectez les valeurs suivantes à ses attributs :
# - user1
#   - firstname: Joe
#   - lastname: Dalton
#   - email: joe.dalton@example.com
#   - newsletter: true
# - user2
#   - firstname: Jack
#   - lastname: Dalton
#   - email: jack.dalton@example.com
#   - newsletter: false
# - user3
#   - firstname: William
#   - lastname: Dalton
#   - email: william.dalton@example.com
#   - newsletter: false
# - user3
#   - firstname: Avrel
#   - lastname: Dalton
#   - email: avrel.dalton@example.com
#   - newsletter: true

# réponse 12.2
user1 = User()
user1.firstname = 'Joe'
user1.lastname = 'Dalton'
user1.email = 'joe.dalton@example.com'
user1.newsletter = True

user2 = User()
user2.firstname = 'Jack'
user2.lastname = 'Dalton'
user2.email = 'jack.dalton@example.com'
user2.newsletter = False

user3 = User()
user3.firstname = 'William'
user3.lastname = 'Dalton'
user3.email = 'william.dalton@example.com'
user3.newsletter = False

user4 = User()
user4.firstname = 'Avrel'
user4.lastname = 'Dalton'
user4.email = 'avrel.dalton@example.com'
user4.newsletter = True
# exo 12.3
# Ajoutez chacune des instances de la classe `User` à une liste nommée `users`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom complet et l'email de chaque utilisateur s'il est abonné à la newsletter

# réponse 12.3
users = [user1, user2, user3, user4]
for value in users:
    print(value.firstname)
    print(value.lastname)
    print(value.email)
    print(value.newsletter)

# exo 12.4
# Créez une classe nommée `ProductLorem` qui possède les attributs suivants :
# - _name: valeur par défaut ''
# - _price: valeur par défaut 0.0
# et les méthodes suivantes :
# - __init__() : le constructeur
# - getName() : renvoit le nom du produit
# - setName() : détermine le nom du produit
# - getPrice() : renvoit le prix du produit
# - setPrice() : détermine le prix du produit

# réponse 12.4

class ProductLorem:
    def __init__(self):
        self._name = ''
        self._price = 0.0

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getPrice(self):
        return self._price

    def setPrice(self, price):
        self._price = price

# exo 12.5
# Créez 3 instances de la classe `ProductLorem` et affectez les valeurs suivantes à ses attributs en utilisant les setters :
# - product1
#   - name: Foo
#   - price: 31,41
# - product2
#   - name: Bar
#   - price: 27,18
# - product3
#   - name: Baz
#   - price: 16,18

# réponse 12.5

product1 = ProductLorem()
product1.setName('Foo')
product1.setPrice(31.41)

product2 = ProductLorem()
product2.setName('Bar')
product2.setPrice(27.18)

product3 = ProductLorem()
product3.setName('Baz')
product3.setPrice(16.18)

# exo 12.6
# Ajoutez chacune des instances de la classe `ProductLorem` à une liste nommée `product_lorems`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom et le prix de chaque produit
# Calculez la somme du prix des produits et affichez-la après la boucle `for`

# réponse 12.6

product_lorems = [product1, product2, product3]
total_price = 0.0
for value in product_lorems:
    print(value.getName())
    print(value.getPrice())
    total_price += value.getPrice()

print(total_price)


# exo 12.7
# Créez une classe nommée `ProductIpsum` qui possède les attributs suivants :
# - _name: valeur par défaut ''
# - _price: valeur par défaut 0.0
# - _tax: valeur par défaut 0.0
# et les méthodes suivantes :
# - __init__(name, price, tax) : le constructeur
# - getName() : renvoit le nom du produit
# - setName() : détermine le nom du produit
# - getPrice() : renvoit le prix du produit
# - setPrice() : détermine le prix du produit
# - getTax() : renvoit la taxe en pourcentage
# - setTax() :  détermine la taxe en pourcentage (20.0 pour une taxe de 20 %)
# - getTaxIncludedPrice() : cette méthode renvoit le prix taxe incluse

# réponse 12.7

class ProductIpsum:
    def __init__(self):
        self._name = ''
        self._price = 0.0
        self._tax = 0.0

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getPrice(self):
        return self._price

    def setPrice(self, price):
        self._price = price

    def getTax(self):
        return self._tax

    def setTax(self, tax):
        self._tax = tax

    def getTaxIncludedPrice(self):
        return (self._tax / 100 + 1) * self._price

# exo 12.8
# Créez 3 instances de la classe `ProductIpsum` et affectez les valeurs suivantes à ses attributs en utilisant le constructeur :
# - product1
#   - name: Dolor
#   - price: 31,41
#   - tax: 20.0
# - product2
#   - name: Sit
#   - price: 27,18
#   - tax: 10.0
# - product3
#   - name: Amet
#   - price: 16,18
#   - tax: 5.5

# réponse 12.8

product1 = ProductIpsum()
product1.setName('Dolor')
product1.setPrice(31.41)
product1.setTax: 20.0

product2 = ProductIpsum()
product2.setName('Sit')
product2.setPrice(27.18)
product2.setTax(10.0)

product3 = ProductIpsum()
product3.setName('Amet')
product3.setPrice(16.18)
product3.setTax(10.0)

# exo 12.9
# Ajoutez chacune des instances de la classe `ProductIpsum` à une liste nommée `product_ipsums`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom, le prix (sans la taxe), la taxe et le produit taxe incluse de chaque produit
# Calculez :
# - la somme du prix des produits sans les taxes
# - la somme du montant des taxes
# - la somme du prix des produits taxes incluses
# Et affichez-les après la boucle `for`

# réponse 12.9

product_ipsums = [product1, product2, product3]
total_price = 0
total_tax = 0
tax_price = 0

for value in product_ipsums:
    print(value.getName())
    print(value.getPrice())
    print(value.getTax())
    print(value.getTaxIncludedPrice())
    total_price += value.getPrice()
    total_tax += (value.getTaxIncludedPrice() - value.getPrice())
    tax_price += value.getTaxIncludedPrice()

print(f'total tax: {total_tax}')
print(f'total price: {total_price}')
print(f'total tout: {tax_price}')