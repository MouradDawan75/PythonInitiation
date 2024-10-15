# Méthode: est un bloc d'instructions réutilisable
# Il existe de 2 types de méthodes:
# Procédure: méthode qui ne renvoie aucun (Ex: print())
# Fonction: méthode qui renvoie un résultat (Ex: input())

# Syntaxe de création d'une fonction: def nom_fonction(paramètres - arguments): instructions

# Exemple d'une fonction:

def fonction1():
    print('appelle de fonction1.....')


fonction1()

# Sans les 2 parenthèses, ce n'est pas un appel de la fonction. Il s'agit d'une variable contenant
# l'id de la fonction en mémoire
print(fonction1)

f = fonction1

f()

# Exemple d'une fonction avec des paramètres:

def repeter(message, nombre_de_fois):
    # Boucle while
    # compteur = 0
    # while True:
    #     compteur += 1
    #     print(message)
    #     if compteur == nombre_de_fois:
    #         break

    # Boucle FOR:
    if nombre_de_fois <= 0:
        print('Attention ce nombre doit être positif')
        while True:
            nombre_de_fois = int(input('Nombre positifs: '))
            if nombre_de_fois > 0:
                iterations = range(nombre_de_fois)

                for i in iterations:
                    if nombre_de_fois <= 0:
                        print('Attention ce nombre doit être positif')
                    else:
                        print(message)
                break
            else:
                print('Uniquement un nombre positif')



repeter('Hello', -100)

# Exemple d'une fonction qui renvoie un résultat:

def somme(x,y):
    return x + y

r = somme(10,15)
print(r)

print(somme('test1','test2'))

#print(somme('test', 5))

# Annotations de types (Depuis Python 3.5): mécanisme qui permet aux développeur de préciser le type des paramètres
# à fournir à une fonction

# Le typage reste dynamique même en pratiquant les annotations de types

x:int = 10
s:str = 'test'

x = 'chaine'

def add(x:int, y:int) -> int:
    return x + y

resultat = add(10,25)

# Bonne pratique: utilisation des annotations de types dans la définition de fonctions