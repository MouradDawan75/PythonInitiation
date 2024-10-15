# Il existe 3 types d'erreurs possibles dans un code:
# - Erreurs de compilation (syntaxe): sont détectées automatiquement par l'IDE (Vs Code)
# - Les exceptions: sont des erreurs qui provoquent l'arrêt de l'application
# - Code fonctionnel qui renvoi un résultat inattendu (faire du debbugage).

# Pour éviter l'arrêt de l'application, on doit gérer l'exception.
# Pour gérer une exception, on utilise le bloc try/except

x = 10

# Il existe plusieurs types d'exceptions, chacune d'elles porte le nom de l'erreur qu'elle
# génère.
# Il existe aussi un type générique qui est le type Exception

try:
    chaine = 'test' + 5
    print(x / 0)
    
except ZeroDivisionError:
    print('bloc except.......')

except TypeError:
    print('exception concaténation gérée....')
    

print(">>>> Utilisation du type générique:")

# Obligation: une ressource (fichier, base de données, Api REST..) doit être libérée à la fin
# de son utilisation.

try:
    chaine = 'test' + 5
    print(x / 2)
    # suite du code ici ou dans le bloc else
    # Ouverture d'un fichier en lecture   
    
    
except Exception as e: # e contient les détails de l'exception
    print('bloc except générique.......')
    print(e)
    

else:
    # bloc optionnel qui s'exécute quee si aucune erreur n'a été générée dans le try
    print('bloc else.........')
    

finally:
    # bloc optionnel qui s'exécute dans tous les cas, exception ou pas.
    print('bloc finally.......')
    # Fermeture du fichier
    # Dans la pratique ce bloc sert à libérer les ressources utilisées dans le try

while True:
    nombre = input("Votre nombre: ")

    try:
        nombre = int(nombre)
        #break

    # syntaxe simplifiée d'utilisation du type générique
    except:
        print('Nombre invalide......')

    else:
        # Tout est ok -> nombre valide
        break


print("suite du programme......")



