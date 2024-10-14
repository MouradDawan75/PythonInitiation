# Variable: zone mémoire contenant une valeur typée
# Types numériques: int, float, complex
# Type textuel: str (string)
# Type boolean: bool (True/False)
# Type listes: range(), tuple, list
# Type ensemble: set
# Type mapping: dict (fonctionne par association clé:valeur)

# Déclaration de variables: en Python, le typage est dynamique. Pas besoin de préciser le type de la variable
# En Java le typage est statique: int x = 10 
# C'est l'interpréteur qui détermine le type de la variabe selon la valeur qu'on lui a affecté 

entier = 10
floattant = 10.5

# Pour les chaines, 2 syntaxes:

chaine = 'ceci est une chaine'
autre_chaine = "autre chaine"
complexe = 1 + 4j # j est le nombre imaginaire

print(entier)
print(floattant)
print(chaine)
print(complexe.real)
print(complexe.imag)

# Conventions de nommage:
# - le nom d'une variable commence soit par une lettre ou un underscore
_x = 10
# PascalCase: MaVariable
# camelCase: maVariable
# snake_case: ma_variable - convetion utilisée dans Python
# variables et fonctions: snake_case
# Classes: PascalCase en Python

##### Contante: est une variable dont on ne peut pas modifier. 
# La notion de constante n'existe pas réellement en Python, c'est pus une convention de nommage

# Le nom d'une constante doit être en majuscules
MA_VALEUR = 10
MA_VALEUR = 'test'

print(MA_VALEUR)

##### Variables nulles:

y = None # None pour null

print(y)

print(">>>>>>>>>>>>> Type d'une variable:")

i = 10
print(type(i))

i = 'test'
print(type(i))

print(">>>>>>> ID des variables:")

# Pour commenter des lignes sélectionnées: ctr + k + c
# Pour décommenter des lignes sélectionnées: ctr + k + u

x = 10
print(id(x))

y = x
print(id(y))

x = 99
print(id(x))

# Pour les nombres réels, on peut faire la chose suivante:

n = 0.99
n = 00.99
n = .99

# Vous pouvez consulter également l’ensemble des raccourcis VSCode :
# https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf

# Pour une meilleure lisibilité des grands nombres, on peut faire la chose suivante:

n = 456_899_123

print(">>>>> Conversion de types:")

i = 10
f = float(i)

print(f)

x = int(f)
s = str(x)

c = '10'
h = int(c)

nb1 = int(input("Premier nombre: "))
nb2 = int(input("Second nombre: "))

s = nb1 + nb2
print("somme = "+str(s)) # En python on ne peut concaténer que des str

