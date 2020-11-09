a = 10
b = 42
print(a, b)
tmp = 0

tmp = a 
a = b
b = tmp
print(a, b)

# OR

a, b = b, a
print(a, b)
