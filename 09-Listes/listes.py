# list: est une collection ordonnée avec doublons autorisés.

# Syntaxes pour créer une liste vide:

l = []
l2 = list()

# Il n'y à aucune restriction sur le type des données d'une liste
# Dans la pratique on manipule des listes cohérentes: liste de user, liste de produits......

lst = [1,2,10.5,'test',[10,20]]

notes = [2,6,7,9]
print(notes)

# Ajouts:

# Types de bases: int,float,bool,str -> sont immuables
# Types complèxes (collections, dates, classes/objets) -> sont muables

notes.append(9)

print(notes)

notes.insert(0,9)
print(notes)

# Modifications:

notes[0] = 15 # modif du contenu de la première case de la liste
print(notes)

# Suppressions:

notes.remove(9)
print(notes)

notes.pop() # supprime le dernier par défaut
print(notes)

# Compter le nombre d'occurrences:
print(notes.count(6))
print(notes.index(15))
#print(notes.index(100)) -> exception car element inexistant dans la liste

print(">>>>> Atteindre un élement d'une liste:")
notes = [2,6,7,9]


taille = len(notes)

print(f'Première note: {notes[0]}')
print(f'Dernière note: {notes[taille-1]}')

# Python autorise les indexs négatifs:

print(f'Dernière note: {notes[-1]}')

print(">>>>> Parcourir une liste:")

print("\t ___ FOR:")

for i in notes:
    print(i)

print("\t ___ While:")

compteur = 0
while compteur < len(notes):
    print(notes[compteur])
    compteur += 1

print("\t ___ For + index:")

for index in range(len(notes)):
    print(notes[index])

print(">>>>>>>>>>>> Slicing:")

# Slicing: mécanisme permettant de créer des sous listes à partir de listes existantes

prenoms = ['Jean','Marc','Marie','Julie']

list1 = prenoms[0:3] # de index 0 (inclus) à index 2 (n - 1)
print(list1)

list2 = prenoms[:3] # du début jusqu'à n - 1
print(list2)

list3 = prenoms[:] # du début à la fin (c'est une copie)
print(list3)

list4 = prenoms[0:3:2] # de index 0 à index 2 avec un pas de 2
print(list4)

list5 = prenoms[::2] # du début jusqu'à la fin avec un pas de 2
print(list3)

print(">>>>>> Comprehension List:")
# Liste en compréhension: mécanisme permettant de créer de nouvelles listes à partir
# de listes exitantes en modifiant le contenu des listes de départ

nombres = range(10) # 0,....,9

# Créer une nouvelle liste à partir de nombres en multipliant par 2 tous les éléments

# Syntaxe classique:
nombres_doubles = []

for e in nombres:
    nombres_doubles.append(e * 2)

# Syntaxe Liste En comprehension: suntaxe simplifiée 

nombres_doubles_new = [e*2 for e in nombres]

# Nouvelle liste à partir nombres ne contenant que les nombres pairs
nombres = range(10)

nombres_pairs = [e for e in nombres if e % 2 == 0]

