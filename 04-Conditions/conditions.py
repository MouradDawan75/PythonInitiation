# Bloc conditionnel: est un ensemble d'instructions qui e s'exécute que si une condition est vraie

age = 26

if age < 18:
    print("Majeur")
    print("Toujours majeur")

print("Fin du bloc if")

# les : (2 points) symbôlisent le début d'un bloc d'instructions.
# Tant que les instructions sont indentées de la mm façon, on est toujours dans le mm bloc

if age < 18:
    print("Mineur")
else:
    print("Majeur")

# Else If:

if age < 18:
    print("Mineur")
elif age <= 25:
    print("Jeune adulte")
else:
    print("Majeur")

# On peut aussi combiner des conditions en utilisant les opérateurs logiques:

if age >= 18 and age <= 25:
    print("Jeune adulte")

# Opérateur ternaire: permet de remplacer le if/else classique, ou de faire des affectations conditionnelles

# if/else classique:

if age < 18:
    print("Mineur")
else:
    print("Majeur")

# Syntaxe ternaire: syntaxe simplifiée

print("Mineur")  if age < 18 else print("Majeur")

# Affectation conditionnelle:

x = None
if age < 18:
    x = 'mineur'
else:
    x = 'majeur'

# Syntaxe tternaire:

x = 'mineur' if age < 18 else 'majeur'

# Un bloc vide n'est pas valide syntaxiquement: néaumoins, il est possible de le définir en utilisant le mot clé pass

if age > 18:
    # a compléter plus tard
    pass


print("la suite......")

# Depuis Python 3.10, ajout du match/case -> syntaxe simplifiée permettant de remplacer les elif qui s'imbriquent

note = 16

match note:

    case 0|1|2|3|4|5|6|7|8|9:
        print("En dessous de la moyenne.....")

    case 10|11|12|13:
        print("Juste la moyenne")

    # Pour les autres cas:
    # Utilisez case other ou case _:

    # case other:
    #     print("Good job")

    case _:
        print("Good job")