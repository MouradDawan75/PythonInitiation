#1) Définir une fonction qui renvoie la somme des éléments d'une liste d'entiers.

# def somme_liste(entiers:list[int]) -> int:

#     s = 0
#     for i in entiers:
#         s += i

#     return s

from myfonctions import somme_liste,moyenne_liste,table_multipication,table_multipication_avec_while,table_multipication_avec_while_finie

print(somme_liste([10,20,30]))

#2) Définir une fonction qui renvoie la moyenne des éléments d'une liste d'entiers.

# def moyenne_liste(entiers:list[int]) -> float:
#     s = somme_liste(entiers)
#     nb_elements = 0
#     for e in entiers:
#         nb_elements += 1

#     return s / nb_elements

print(moyenne_liste([1,2]))

#3) Ecrire une fonction qui affiche la table de multiplication d'un nombre où le premier et 
# le dernier multiple sont des params de la fonction.
# Ex: table_multiplication(13,1, 11)

print("========================Exo 3: FOR============================")

# def table_multipication(nombre, premier_multiple, dernier_multiple):
#     for i in range(premier_multiple, dernier_multiple + 1):
#         print(f"{nombre} x {i} = {nombre * i}")


table_multipication(9,1,15)

print("========================Exo 3: While True============================")

# def table_multipication_avec_while(nombre, premier_multiple, dernier_multiple):
#     i = 0
#     while True:
#         print(f"{nombre} x {premier_multiple + i} = {nombre * (premier_multiple + i)}")
#         i += 1
#         if i == dernier_multiple:
#             break

table_multipication_avec_while(9,1,15)  


print("=========================While finie=========================") 

# def table_multipication_avec_while_finie(nombre, premier_multiple, dernier_multiple):
#     i = 0
#     while i < dernier_multiple:
#         print(f"{nombre} x {premier_multiple + i} = {nombre * (premier_multiple + i)}")
#         i += 1
    
      

table_multipication_avec_while_finie(9, 1, 15)