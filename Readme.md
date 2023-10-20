# TD1

## Aperçu

Ce document explique la logique du pipeline, le contenu des différents fichiers, et comment utiliser le service composite.

NB : Dans cette version, le texte est fourni par le client (soap_client.py) en tant que paramètre du service sous forme de chaîne de caractères. Par conséquent, cette version ne prend pas en compte l'observateur.

## Fichiers

Voici les fichiers présents dans le projet :

1. `loanService.py`: Ce fichier contient notre service composite.
2. `Property_Evaluation_Service.py`: Il contient la définition du service qui s'occupe de l'évaluation de la propriété.
3. `Text_Extraction_Service.py`: Il contient la définition du service responsable d'extraire les informations essentielles contenues dans le texte.
4. `Solvency_Verification_Service.py`: Il contient la définition du service qui effectue la vérification de la solvabilité du client.
5. `other_services.py`: Ce fichier déploie les trois services qui seront utilisés par le service composite.
6. `soap_client.py`: C'est le client qui fait appel au service composite.
7. `observer.py`: (Belkis, je te laisse expliquer)

## Pipeline

Les trois services (`Property_Evaluation_Service.py`, `Text_Extraction_Service.py`, `Solvency_Verification_Service.py`) sont déployés en exécutant le fichier `other_services.py`. Le service composite est déployé en exécutant le fichier `loanService.py`.

Lorsqu'un client (`soap_client.py`) fait appel à l'application composite (`loanService.py`), celle-ci fait appel aux différents services (`Property_Evaluation_Service.py`, `Text_Extraction_Service.py`, `Solvency_Verification_Service.py`) pour déterminer si le client peut avoir droit au prêt ou pas (le résultat est affiché en ligne de commande).

## Utilisation

1. Ouvrez un terminal et exécutez la commande : `python3 other_services.py`
2. Ouvrez un autre terminal et exécutez la commande : `python3 loanService.py`
3. Ouvrez un autre terminal et exécutez la commande : `python3 soap_client.py`