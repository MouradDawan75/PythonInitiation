# Approche procédurale: repose sur l'utilisation des params et des fonctions
# Approche objets: repose sur l'utilisation de classes et objets

# Une classe est un type de données. Elle a pour tâche principale de décrire la structure d'un objet.
# Elle définie une sorte de template à partir duquel on crée nos objets

# Elle contient généralement 3 choses:
# - Attributs - propriétés: représentent l'état de l'objet
# - fonctions: représentent le comportement de l'objet
# - fonction spéciale qui porte le nom de la classe, appelée constructeur (initialisateur)
# permettant d'instancier la classe en question.


class User:

    def __init__(self,nom,prenom):
        # self: mot clé qui pointe vers l'objet en cours d'tilisation
        self.nom = nom
        self.prenom = prenom
        print('*********************')

    def afficher_nom(self):
        print(f'Nom: {self.nom}')


    #__str__: fonction qui permet de personnaliser l'affichage d'un obej. Choisir 
    # les attributs à afficher
    def __str__(self):
        return f'Nom: {self.nom} - Prénom: {self.nom}'
    
    #__eq__: permet de choisir les critères d'égalité de 2 objets
    def __eq__(self, other):
        return self.nom == other.nom



# Code exécuté par Python en arrière plan
u = User('DUPONT','Jean')

u.afficher_nom()

u2 = User('ZIDANE','zizou')
u2.afficher_nom()

print(u)

u3 = User('DUPONT','Jeansdqsdsq')

print(u == u3)

class CompteBancaire:


    def __init__(self,numero,solde):
        self.numero = numero
        self.solde = solde

    def depot(self,montant):
        self.solde += montant

    def retrait(self,montant):
        if self.solde >= montant:
            self.solde -= montant
        else:
            print("Solde insuffisant......")

    def __str__(self):
        return f'Numéro: {self.numero} - Solde: {self.solde}'
    
    def __eq__(self, other):
        return self.numero == other.numero
    

cpt = CompteBancaire('dsd1450', 1000)
cpt.depot(500)
cpt.retrait(350)

print(cpt)

