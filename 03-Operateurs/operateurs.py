print("************ Opérateurs arithmétiques:")

print("\t Addition:")

a = 5
b = 2
c = a + b
c += 2 # syntaxe simplifiée -> equivalent c = c + 2

print(f"c = {c}")

print("\t Soustraction:")

a = 5
b = 2
c = a - b
c -= 2 # syntaxe simplifiée -> equivalent c = c - 2

print(f"c = {c}")

print("\t Multiplication:")

a = 5
b = 2
c = a * b
c *= 2 # syntaxe simplifiée -> equivalent c = c * 2

print(f"c = {c}")

print("\t Division:")

a = 5
b = 2
c = a / b
c /= 2 # syntaxe simplifiée -> equivalent c = c / 2

print(f"c = {c}")

print("\t Division entière:")

a = 5
b = 2
c = a // b
c //= 2 # syntaxe simplifiée -> equivalent c = c // 2

print(f"c = {c}")

print("\t Modulo: reste de la division entière")

a = 5
b = 2
c = a % b
c %= 2 # syntaxe simplifiée -> equivalent c = c % 2

print(f"c = {c}")


print(5 / 2) # division classique -> 2.5
print(5 // 2) # division entière: renvoie uniquement le quotient -> 2
print( 5 % 2) # moduo -> reste de la divison entière -> 1

print("\t Puissance:")

a = 5
b = 2
c = a ** b # a puissance b
c **= 2 # syntaxe simplifiée -> equivalent c = c ** 2

print(f"c = {c}")

print("**************** Opérateurs de comparaison:")

# > >= < <= == (égalité) != (différent)
# Ces opérateurs renvoient un boolean

a = 5
b = 7

print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)

resultat = a == b # comparaison
print(resultat) # False


a = b # affectation
print(a)

resultat = a == b # comparaison
print(resultat) # True

print("****************** Opérateurs logiques:")
# and, or et not
# Table logique:

# A     B       A and B     A or B
# v     f          f          v
# v     v          v          v
# f     f          f          f
# f     v          f          v

a = 5 
b = 7

print((a > 0) and (a > b)) # False
print((a > 0) and (a < b)) # True
print((a < 0) and (a > b)) # False

print(not(a > 0))
print(not(True))
print(not(False))

print("************** Affectations multiples:")

# Si des variables sont du mm type et possèdent la mm valeur, on peut faire:

v1=v2=v3=10
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v3 = {v3}")

# Si des variables ne sont pas du mm type, on peut faire: non recommandée dans la pratique

var1,var2,var3 = 10,True,'test'

print(f"var1 = {var1}")
print(f"var2 = {var2}")
print(f"var3 = {var3}")

print("************* Opérateurs: is, in")

list1 = [1,2,3]
list2 = [1,2,3]

print(list1 == list2) # True: car le mm contenu

print(list1 is list2) # False: car 2 objets différents en mémoire

print(id(list1))
print(id(list2))

print("******************************")

list3 = list1
print(list1 is list3) # True: car les 2 variables pointent vers le mm objet en mémoire

print(id(list1))
print(id(list3))

# L'opéreteur permet de vérifier si un élément fait partie ou pas d'une collection

print(1 in list1)
print(5 in list2)

chaine = "ceci est une chaine" # une chaine (str) par définition est une collection de caractéres

print('ceci' in chaine)
print("Ceci" in chaine) # Python est sensible à la casse: x et X sont 2 variabes différentes


list1 = [1,2,3]
list4 = [1,2]
print(list4 in list1) # False: car list1 ne contient que des int alors que list4 n'est pas un int, c'est liste de int


list5 = [1,2,3,[1,2]]
list6 = [1,2]

print(list6 in list5)

# Pour des calculs complèxes, on peut utiliser les modules math,statistics

import math,statistics

math.sqrt(25)
statistics.mean(list1)