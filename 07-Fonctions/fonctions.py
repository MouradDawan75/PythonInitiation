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



#repeter('Hello', -100)

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
print(">>>>>>>>>>>>>> Fonction avec des params optionnels:")

# Les params optionnels possèdent une valeur par défaut et sont définis après les params
# obligatoires

# Objectifs: obtenir un code facile à étendre

def fct(x, alpha=10, beta=11):
    print(x,alpha,beta)

fct(55) # alpha et beta non nécessaires lors de l'appel car possèdent une valeur initiale
fct(55,33,44) # on peut modifier les valeurs initiales des params optionnels en cas de besoin

# Appel d'une fonction avec des paramètres nommés sans tenir compte de leur position dans
# la fonction



fct(beta=150,x=66)

print('chaine1', end=" ")
print('chaine2')

def prix_ttc(prix_ht:float, tva:float = 0.2) -> float:
    return prix_ht * (1 + tva)

print(prix_ttc(80))
print(prix_ttc(80, tva=0.35))

print(">>>>>>>>>>>>>>> Fonction qui renvoie plusieurs résultats:")

def calculs(x:int, y:int):
    somme = x + y
    produit = x * y
    moyenne = (x + y) / 2
    return somme,produit,moyenne
    #return produit -> on ne peut avoir qu'un seul return dans une fonction

resultat = calculs(10,20)

print(type(resultat))
print(resultat)

# Eclatement d'un tuple
addition,produit,moyenne = resultat
print(f"Somme = {addition}")
print(f"Produit = {produit}")
print(f"Moyenne = {moyenne}")

a,b,c = calculs(15,16)
print(a,b,c)

print(">>>>>>>>> Fonction avec un nombre variable de paramètres:")

print(10,True, 'Test', [1,2])

def somme_variable(*entiers:int) -> int:
    # entiers est un tuple à taille variable
    """
    C'est une fonction qui renvoie la somme d'un nombre
    variable d'entiers
    """

    s = 0
    for e in entiers:
        s += e

    return s

print(somme_variable(10,20))
print(somme_variable(10,20,30))
print(somme_variable(10,20,30,40))

print(">>>>>>>>>>>> Variables: locales et globales")

# b,c sont des variables globales: visibles dans tout le script

b = 10
c = 10

def test():

    # Les variables définies dans une fct sont appelées variables locales
    # Visibles uniquement dans la fct

    global b # demande explicite à fct de manipuler le b global
    b = 15
    c = 15
    v = 10
    print("**********************************")
    print(locals())
    print("**********************************")

test()


print(f"b = {b}")
print(f"c = {c}")

print(globals())

print(">>>>>> Fonctions natives de Python:")

lst = [1,2,3]

print(sum(lst))
print(min(lst))
print(max(lst))
print(len(lst)) # renvoie la taille d'une collection
print(round(2.4589,ndigits=2))
