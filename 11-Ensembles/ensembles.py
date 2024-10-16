# Set (ensemble): est une collection non ordonnée sans doublons
# De plus, le type set supporte les opérations sur les ensembles telles que l'union,
# l'intersection, la différence et la différence symétrique

# Syntaxe pour créer un set vide:
s = set()

panier = {"apple","banana","apple","orange"}
print(panier)

a = set('abracadabra') # conversion d'une chaine en set
b = set('alacazam')

print(a)
print(b)

l = list('abracadabra') # conversion d'une chaine en list
print(l)

print(">>>> Union:")
# 2 syntaxes: lettres dans a ou dans b ou dans les 2
print(a | b)
print(a.union(b))

print(">>>> Intersection:")
# 2 syntaxes: lettres dans a et dans b
print(a & b)
print(a.intersection(b))

print(">>>> Différénce:")
# 2 syntaxes: lettres dans a mais pas dans b
print(a - b)
print(a.difference(b))

print(">>>> Différence symétrique:")
# 2 syntaxes: lettres dans a ou dans b mais pas dans les 2
print(a ^ b)
print(a.symmetric_difference(b))

# Le type set supporte la syntaxe ensemble en compréhension
ensemble = set('abracadabra')

# un nouvel ensemble ne contenant que les lettres différentes de a,b et c
new_ensemble = {lettre for lettre in ensemble if lettre not in 'abc'}

# Suppression de doublons dans une liste
lst = [1,1,2,2,3,3]
lst = set(lst)
lst = list(lst)
print(lst)