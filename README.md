# domainavailable
Script permettant de vérifier si un ou plusieurs domaines sont utilisés.
Il permet aussi de chercher une liste de nom de domaine nom utilisé   en utilisant plusieurs arguments

# Utilisation
Liste des arguments du script:
-t permet d'indiquer le TLD (Top level domain) par exemple .com
-d permet d'indiquer une liste d'argument qui seront liers ensemble pour la recherche

# Exemple
domainavailable.py -t .com -d security,internet,network
La commande donnera:
securityinternet.com securitynetwork.com internetsecurity.com internetnetwork.com networkinternet.com networksecurity.com

Si vous ne renseigné pas l'argument -d les domaines seront testés avec les tld suivant:
.com .fr .net .org .int .info .paris .edu .uk
