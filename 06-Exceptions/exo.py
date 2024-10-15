
import random

aleatoire = random.randint(1,100)

i = 0
print('Devinez le nombre aléatoire compris entre 1 et 100')

while True:

    nombre = input("Votre nombre: ")
    i += 1
    if i == 6:
        print('Dernière tentative')
    else:
        print(f'{i} tentative')
    try:
        nombre = int(nombre)
        
        if nombre == aleatoire:
            print(f'Trouvé en {i} tentatives. Aléatoire = {aleatoire}')
            break

        if i == 6:
            print(f'Perdu! nombre alétoire est: {aleatoire}')
            break

        if nombre > aleatoire:
            print('Plus petit')
        else:
            print('Plus grand')


    except:
        print('Nombre invalide.....')

print(">>>>>>>>>>>> avec une boucle for:")

# Si le nombre d'itérations est connu, on peut utiliser la boucle for avec la fonction range
# pour gérer le nombre d'itérations.

#nb = int(input('Nombre de tentatives max: '))

for i in range(1,7):

    nombre = input("Votre nombre: ")
    try:
        nombre = int(nombre)
        
        if nombre == aleatoire:
            print(f'Trouvé en {i} tentatives. Aléatoire = {aleatoire}')
            break

        

        if nombre > aleatoire:
            print('Plus petit')
        else:
            print('Plus grand')


    except:
        print('Nombre invalide.....')