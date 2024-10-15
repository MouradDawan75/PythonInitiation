
import random

random.randint(1,10)

# On peut aussi modifier le nom du module importé -> définir un alias

import random as rd

rd.randint(1,10)

# On peut aussi importer des éléments spécifiques à partir d'un module

from math import sqrt,cos

sqrt(25)

# On peut aussi modifier le nom des éléments importés

from math import sqrt as racine_carree

racine_carree(16)

# On peut aussi importer tous les éléments d'un module

from math import * # on doit connaitre toutes les fonctions du modue

sqrt(16)

import math

# On doit préfixer la fonction avec le nom du module
math.sqrt(16)

# Un module est un fichier.py qui contient généralement des fonctions, des classes ou des constantes
# Un package est un répertoire contenant des modules.

# Important: le nom d'un package ou d'un module doit être en miniscules, sans espaces, sans
# underscore, sans le trait d'union et doit commencer par une lettre

# Pour convertir un dossier en package Python, ce dernier doit contenir le fichier __init__.py
# qu'on peut laisser vide.

# Pour Python < 3.3: __init__.py est obligatoire
# Pour Python >= 3.3: __init__.py n'est pas obligatoire, mais il est recommander de le 
# générer comme même.

# __init__.py pourrait servir à initialiser des variables globales
# Le contenu de ce fichier est toujours exécuté en premier lors d'un import

# Appeler fonction1 définie dans mymodule.py

#from mypackage import mymodule -> tout le module

from mypackage.mymodule import fonction1 # -> fonction 
from mypackage import myconstantes

#from mypackage import mymodule

# Un module importé est toujours exécuté
# Comment empêcher l'exécution d'un module importé?
# fonction1()

# __name__ = '__main__' pour un module exécuté
# __name__ = 'nom_module' pour un module importé

#print(__name__)

print(myconstantes.SERVER)
print(myconstantes.PORT)
print(myconstantes.USER)
print(myconstantes.PASSWORD)

# Exo:
# Dans le dossier principal:
# - Créez un package nommé mytools contenant le module myfonctions.py
# - Ajoutez dans le module une fonction add(x,y)
# - Importez et testez la fonction add dans ce fichier

# La liste des chemins des modules (packages) visibles par Python est définie dans sys.path


import sys
import os # Facilite la gestion des paths

print(sys.path)

#chemin = 'C:\Users\Admin\Desktop\PythonInitiation'

#sys.path.append(chemin)

print(__file__) # c:\......\modules.py

#chemin_dossier_en_cours = os.path.dirname(__file__) # c:\.....\08-Modules
#chemin_dossier_principal = os.path.dirname(chemin_dossier_en_cours) # c:\...\PythonInitiation

chemin_dossier_principal = os.getcwd() # getcwd: Get Current Working Directory: renvoie le chemin du dossier principal

print(chemin_dossier_principal)

sys.path.append(chemin_dossier_principal)


# Solution: ajoutez le chemin du dossier pricncipal dans sys.path

# chemin = 'c:\......\PythonInitiation'

from mytools.myfonctions import add

print(add(5,10))

# pip: est le gestionnaire de modules externes en Python
# pip install nom_module
# pip uninstall nom_module
# pip list

# pip install streamlit