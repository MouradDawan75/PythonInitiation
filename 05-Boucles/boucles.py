print("********* Bloc itératif:")

# est un boc d'instructions qui peut être répété un certain nombre de fois
# Si le nombre d'itérations est connu, on utilise la boucle for.
# Si ce n'est pas connu, mais que le bloc d'instructions dépend d'une condition, on utilise la boucle while

# La boucle FOR: permet de parcourir tous les éléments d'une collection
# La boucle WHILE (boucle conditionnelle): permet d''exécuter un bloc d'instructions tant qu'une condition est vraie
# 
print("*** Boucle FOR:")

nombres = range(10) # renvoie une collection d'entiers allant de 0 à  n - 1 (9)

# Pour chaque élément e contenu dans nombres
for e in nombres:
    if e == 5:
        break
    print(e)


chaine = 'test'

for lettre in chaine:
    print(lettre)

print("*** Boucle WHILE:")

x = 0

while x < 5:
    print(x)
    x += 1 # x = x + 1
    if x == 3:
        break

# Demandez la saisie d'un nombre compris entre 1 et 10. Tant que le nombre saisi n'est pas valide, le user doit 
# saisir un autre.


# Solution sans boucle infinie:

print(">>> Boucle finie:")

i = 0
while not(i >= 1 and i <= 10):
    i = int(input("Nombre compris entre 1 et 10: "))



print(">>> Boucle infinie:")

# Solution avec une boucle infinie: le break est nécessaire
while True:
    nb = int(input("Un nombre entre 1 et 10: "))
    if nb >= 1 and nb <= 10:
        break


# random: module permettant de générer des nombres aléatoires
import random

a = random.randint(1,10)
print(a)

print(">>>>> Break et Continue:")

prenom = "sylvain"

for lettre in prenom:
    if lettre == 'y':
        continue # force le passage à l'itération suivante -> la suite de la boucle n'est pas exécutée

    if lettre == 'i':
        break

    print(lettre) # slva

