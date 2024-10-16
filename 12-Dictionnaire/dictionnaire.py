# dict: est une collection non ordonnée qui fonctionne par association clé:valeur
# Dans un dictionnaire physique, le mot est la clé, sa définition est la valeur
# Dans un dict les clés sont uniques.

# Syntaxe pour créer un dict vide:
d = dict()
d1 = {}

# Un dictionnaire peut être utilisé pour regrouper les caractéristiques d'un objet

user = {
    "nom": "DUPONT",
    "prenom": "Jean"
}

print(user)

print(user["nom"])
#print(user["Nom"]) -> si clé inéxistante -> exception

print(user.get("nom"))
print(user.get("Nom")) # si clé inéxistante- > renvoie None

user['contrat'] = 'CDD' # si clé inéxistante -> elle est créée
print(user)

user['contrat'] = 'CDI' # si la clé existe -> elle ecrasée
print(user)

# On peut avoir des dicts complèxes

utilisateur = {
    "nom": "DUPONT",
    "prenom": "Jean",
    "age": 65,
    "telephones": ["06060606","07070707"],
    "adresse": {
        "rue": "10 rue Machin",
        "code_postal": 75015
    }
}

# Affichez chaque numéro de tél:

for t in utilisateur.get('telephones'):
    print(t)

# Affichez la rue:

print(utilisateur.get('adresse').get('rue'))

# Affichez le 1er num de tél:

print(utilisateur.get('telephones')[0])

print(">>>>>>>>>>>>>>>>> API REST:")

# Web Service SOAP: protocole d'echanged e méssages codés en xml
# API Rest: est un style d'architecture
# Les api rest ne sont pas limitées au format JSON (Javascript Object Naming): xml, texte,  fichier...

# API REST (WEB SERVICE REST): c'est un ensemble de ressources (images, article d'un journal...)
# où chaque ressource possède un id (URI: Uniform Resource Identifier - end point), une 
# mèthode d'accès (GET-DELETE-POST-PUT) et elle peut publique ou privée.

# Toutes ces infos sont fournies dans la doc de l'API

# Pour faire appel à des API Rest en Python, on utilise le module requests
# pip install requests

# import requests

# URI = 'https://restcountries.com/v3.1/all'

# reponse = requests.get(URI).json() # json: fonction pour formatter le contenu en json

# #print(reponse) c'est une liste de dict

# country = input("Votre pays: ")

# for pays in reponse:
#     if pays.get('name').get('common') == country:
#         print(f'Nom: {pays.get('name').get('common') } - Capitale: {pays.get('capital')} - Population: {pays.get('population')}')


print(">>>>> Parcourir un dictionnaire:")

d = {
    'a':1,
    'b':2
}

print(">> For:")

# Le for par défaut renvoie uniquement les clés

for element in d:
    print(element)


print(">> for explicite sur les clés:")
for cle in d.keys():
    print(f"Clé: {cle} - Valeur: {d.get(cle)}")


print(">>> for expicite sur les valeurs:")
for v in d.values():
    print(v)

print(">>> for sur les items:")
for i in d.items():
    print(i) # i est un tuple: (cle,valeur)

# Eclatement du tuple:

for k,v in d.items():
    print(f'Clé: {k} - Valeur: {v}')


print(">>>>> Dictionary Comprehension")

d = {
    'a':1,
    'b':2
}

# Inverser ce dict:

dictionnaire = {v:k for k,v in d.items()}

print(dictionnaire)

d = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}

# Un nouveau dict dont en doublons les valeurs

new_dict = {k:v*2 for k,v in d.items()}
print(new_dict)

nombres = range(10)

# Nouveau dict dont les clés sont les nombres pairs et les valeurs sont les clés puissance 2

resultat = {e:e**2 for e in nombres if e % 2 == 0}

print(resultat)

print(">>>> Multiples conditions:")

d = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e': 5,
    'f': 6
}

# Nouveau dict avec les valeurs paires et supérieures à 2

r = {k:v for k,v in d.items() if v % 2 == 0 if v > 2}

print(r)

