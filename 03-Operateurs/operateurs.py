print("************ Opérateurs arithmétiques:")

print("\t Addition:")

a = 5
b = 2
c = a + b
c += 2 # syntaxe simplifiée -> equivalent c = c + 2

print(f"c = {c}")

print("\t Soustraction:")

a = 5
b = 2
c = a - b
c -= 2 # syntaxe simplifiée -> equivalent c = c - 2

print(f"c = {c}")

print("\t Multiplication:")

a = 5
b = 2
c = a * b
c *= 2 # syntaxe simplifiée -> equivalent c = c * 2

print(f"c = {c}")

print("\t Division:")

a = 5
b = 2
c = a / b
c /= 2 # syntaxe simplifiée -> equivalent c = c / 2

print(f"c = {c}")

print("\t Division entière:")

a = 5
b = 2
c = a // b
c //= 2 # syntaxe simplifiée -> equivalent c = c // 2

print(f"c = {c}")

print("\t Modulo: reste de la division entière")

a = 5
b = 2
c = a % b
c %= 2 # syntaxe simplifiée -> equivalent c = c % 2

print(f"c = {c}")


print(5 / 2) # division classique -> 2.5
print(5 // 2) # division entière: renvoie uniquement le quotient -> 2
print( 5 % 2) # moduo -> reste de la divison entière -> 1

print("\t Puissance:")

a = 5
b = 2
c = a ** b # a puissance b
c **= 2 # syntaxe simplifiée -> equivalent c = c ** 2

print(f"c = {c}")

print("**************** Opérateurs de comparaison:")

# > >= < <= == (égalité) != (différent)
# Ces opérateurs renvoient un boolean

a = 5
b = 7

print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)

resultat = a == b # comparaison
print(resultat) # False


a = b # affectation
print(a)

resultat = a == b # comparaison
print(resultat) # True