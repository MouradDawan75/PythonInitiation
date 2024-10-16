# tuple: est une collection ordonnée avec doublons autorisés, non modifiable
# Liste en lecture seule (liste constante)

# Syntaxe pour créer un tuple vide:
t = tuple()
t1 = ()

prenoms = ('Jean','Marc','Marie')
print(prenoms.count('Jean'))
print(prenoms.index('Jean'))

print(prenoms[0])

# prenoms[0] = 'Dawan' -> exception
# Modification d'un tuple:

# 1 - Conversion en liste
prenoms = list(prenoms)

# 2 -Application des modifications
prenoms.append('Dawan')
prenoms.append('Paris')
prenoms.remove('Jean')

# 3 - Conversion en tuple
prenoms = tuple(prenoms)

print(prenoms)

# Eclatement d'un tuple -> car sa taile est fixe
p1,p2,*reste = prenoms
print(p1)
print(p2)
print(reste)

p1,p2,p3,p4 = prenoms

def test():
    while True:

        respone = input('Pour quitter tapez q : ')
        if respone == 'q':
            return # fonctionne comme un break
        
test()