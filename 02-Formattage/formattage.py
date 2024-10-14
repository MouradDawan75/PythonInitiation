age = 50
prenom = "Marie"

# Concaténation: on doit convertir les types numériques en str

print("Prénom: "+prenom+" Age: "+str(age))

# On peut utiliser la virgule comme séprateur: pas besoin de convertir es types numériques en str, de plus
# la virgule génère un éspace

print("Prénom:",prenom,"Age:",age)

# A partir de Python 3: ajout de la fonction format

print("Prénom: {} Age: {}".format(prenom,age))

s = "Prénom: {} Age: {}".format(prenom,age)
print(s)

# Depuis Python 3.6: ajout de fstring -> syntaxe simplifiée de la fonction format

print(f"Prénom: {prenom} Age: {age}")

# Entre accolades, on peut insérer soit des variables, soit des expressions

print(f"{3+5}") # exempe d'une expression
print(f"{float(10)}") # exempe d'une expression

x = 5
y = 6

s = x + y

print(f"Somme = {s}")

print("*********** Chaines sur plusieurs lignes:") # chaine verbatime

print("""
    ceci est une
chaine sur
plusieurs lignes.
""")

# Caractères d'échappement:
# \n: retour à la ligne -> new line
# \r: retour à la ligne -> return
# \t: tabulation
# \s: space
# \b: backspace
# \\: echapper le \
# \": echapper le "
# \': echapper le '

print("\tceci est une\nchaine sur\nplusieurs lignes")

chemin = "c:\\test\\notes.txt"

s = "ceci est \"une\" chaine"
print(s)

c = "l'entrée"
c = 'l\'entrée'
print(c)