#1)Construire une liste ne contenant que les nombres positifs

print(">>>>>>>>>>>>>> EXO 1<<<<<<<<<<<<<<<<<<<<<")
entiers = range(-10,10)

nombres_positifs = [e for e in entiers if e > 0] # Dans le cas d'un if seul, le for arrive en premier

print(nombres_positifs)

#2)Construire une liste en inversant uniquement les nombres impairs
#Résulat attendu: 0,-1,2,-3,4,-5.......
print(">>>>>>>>>>>>>> EXO 2<<<<<<<<<<<<<<<<<<<<<")
entiers = range(10)

# Dans le cas d'un if/else, le for arrive en dernier
nombres_inverses = [e if e % 2 == 0 else -e for e in entiers]
print(nombres_inverses)

print(">>>>>>>>>>>>>> EXO 3<<<<<<<<<<<<<<<<<<<<<")
#3) Affichez le nombre d'éléments supérieurs à 3 (syntaxe liste en compréhension)
lst = [1,3,7,5,9]

print(len([e for e in lst if e > 3]))


print(">>>>>>>>>>>>>> EXO 4<<<<<<<<<<<<<<<<<<<<<")
#4) Définir une fonction qui renvoie la somme des nombres pairs distincts d'une liste d'entiers

def somme_distincts(entiers:list[int]) -> int:
    # Suppression des doublons
    # Construire une liste ne contenant que les nombres pairs distincts
    lst = []
    for e in entiers:
        if e % 2 == 0 and e not in lst:
            lst.append(e)

    return sum(lst)

print(somme_distincts([2,2,4,6,4,8]))

print(">>>>>>>>>>>>>> EXO 5<<<<<<<<<<<<<<<<<<<<<")
#5) Créez une liste qui est la différence entre ces 2 listes

listA = [1,2,3,4]
listB = [1,2]

difference = [e for e in listA if e not in listB] 

