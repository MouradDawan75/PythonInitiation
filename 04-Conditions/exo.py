#1)

nombre = int(input("Votre nombre: "))

if nombre % 2 == 0:
    print(f"{nombre} est pair")
else:
    print(f"{nombre} est impair")

# Syntaxe ternaire:

print(f"{nombre} est pair") if nombre % 2 == 0 else print(f"{nombre} est impair")

#2)

mot = input("Votre mot: ")

if 'e' in mot:
    print(f"{mot} contient e")
else:
    print(f"{mot} ne contient pas e")

# Syntaxe simplifiée:

print(f"Le mot {mot} contient la lettre e ? :  {'e' in mot}")