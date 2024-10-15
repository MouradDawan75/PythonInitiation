#1) Affichez tous les nombres de 1 (inclus) à 15 (inclus) -> fonction range()

print(">>>>>>>>>>>>>>>>> Exo1 <<<<<<<<<<<<<<<<<<<<<<<<<<")

print(">>>>> Solution 1:")

for e in range(16):
    if e != 0:
        print(e)

# Solution2:

print(">>>>> Solution 2:")

for e in range(15):
    print(e+1)

# Solution3: on peut aussi modifier l'index de début -> range commence à 0 par défaut

print(">>>>> Solution 3:")

for e in range(1,16):
    print(e)


#2) Affichez tous les nombres pairs de 1 (inclus) à 10 (inclus) -> fonction range()

print(">>>>>>>>>>>>>>>>> Exo2 <<<<<<<<<<<<<<<<<<<<<<<<<<")

print(">>>>> Solution 1:")

for e in range(1,11):
    if e % 2 == 0:
        print(e)

print(">>>>> Solution 2:")

# On peut aussi modifier le pas de range -> par défaut il est de 1:

for e in range(2, 11, 2):
    print(e)


#3)

print(">>>>>>>>>>>>>>>>> Exo3 avec une boucle finie:<<<<<<<<<<<<<<<<<<<<<<<<<<")

# Définir la condition pour que la boucle s'exécute au moins une fois

choice = 'x'

while choice != 'q':

    choix = input("""

                Menu:
                - Addition: tapez a
                - Soustraction: tapez s
                - Multiplication: tapez m
                - Division: tapez d
                - Quitter: tapez q

                Votre choix ?

            """)
    

    if choix not in ['a','s','m','d']:
        print("Choix invalide....")
        continue

    # if choix not in 'asmd':
    #     print("Choix invalide....")
    #     continue

    nb1 = float(input("Premier nombre: "))
    nb2 = float(input("Second nombre: "))

    match choix:

        case 'a':
            print(f"{nb1} + {nb2}  = {nb1 + nb2}")

        case 's':
            print(f"{nb1} - {nb2}  = {nb1 - nb2}")

        case 'm':
            print(f"{nb1} x {nb2}  = {nb1 * nb2}")

        case 'd':
            print(f"{nb1} / {nb2}  = {nb1 / nb2}")

print(">>>>>>>>>>>>>>>>> Exo3 avec une boucle infinie:<<<<<<<<<<<<<<<<<<<<<<<<<<")

while True:
    choix = input("""

                Menu:
                - Addition: tapez a
                - Soustraction: tapez s
                - Multiplication: tapez m
                - Division: tapez d
                - Quitter: tapez q

                Votre choix ?

            """)
    
    if choix == 'q':
        break

    if choix not in ['a','s','m','d']:
        print("Choix invalide....")
        continue

    # if choix not in 'asmd':
    #     print("Choix invalide....")
    #     continue

    nb1 = float(input("Premier nombre: "))
    nb2 = float(input("Second nombre: "))

    match choix:

        case 'a':
            print(f"{nb1} + {nb2}  = {nb1 + nb2}")

        case 's':
            print(f"{nb1} - {nb2}  = {nb1 - nb2}")

        case 'm':
            print(f"{nb1} x {nb2}  = {nb1 * nb2}")

        case 'd':
            print(f"{nb1} / {nb2}  = {nb1 / nb2}")

#4)

print(">>>>>>>>>>>>>>>>> Exo4 <<<<<<<<<<<<<<<<<<<<<<<<<<")

while True:
    choix = input("""

                Menu:
                1- Convertir minutes en heures
                2- Quitter

                Votre choix ?

            """)
    
    if choix == '2':
        break

    if choix == '1':
        minutes = int(input('Nombre de minutes: '))
        print(f"{minutes}m = {minutes // 60}h {minutes % 60}m")
    else:
        print('Choix invalide......')
