import readchar
from readchar import readkey, key
import os
import json
import csv
from colorama import Back, Fore, Style, deinit, init

"""
bibliothèques authorisées: os, json, csv, colorama, readchar
docu colorama: https://he-arc.github.io/livre-python/colorama/index.html
docu json, csv, os: chatgpt car docus trop longues ou spécifiques
docu readchar: https://github.com/magmax/python-readchar (lire les touches claviers)
"""

"""
Idée de structure du code V1:

Quasiment tout ce qui est codé est dans une fonction (le prof adore)
une grosse fonction qui vient appeler chaque fonction dans l'ordre et en fonction des choix de l'utilisateur
Généraliser le code pour que les petites actions comme ouvrir un csv soient fonctionnel pour tous les csv par ex
Utiliser chatgpt pour trouver une ligne de code ou un petit bout mais pas + ça marchera pas ou ça se verra
(commenter assez régulièrement si vous codez à plusieurs sur le code)


fonctionPrincipale: boucle de jeu qui itère l'avancée du projet (while...) avec l'appel des fonctions etc 
entrées: aucune
sorties: aucune

fonction1: lancer la page d'accueil et attendre que l'utilisateur clicke sur 'enter' (ou 'q')
entrées: aucune
sorties: aucune 

fonction2: lancer le menu et attendre que l'utilisateur clicke sur '1'-'5' (ou 'q')
entrée: 
    partie en cours (bool: oui ou non)--> griser continuer une partie si 'false' 
    scores déja enregistrés (bool: oui ou non)--> pareil pour afficher scores
sorties: aucune 

fonction3-6: lancer le mode de jeu chosisi (1-4 du menu) 
entrées: ça dépend
sorties: ça dépend

fonctionsDeJeu: fonctions qui seront utiles au fonctionnement du jeu pendant 
la partie (faire avancer, écouter clavier,piocher carte, etc...)

fonctionActivationDebogage: si clicke sur 'd' pendant la partie alors mode débogage
entrée: 
    tableau de jeu actuel avec toutes les infos (liste je pense) 
    ActivationDebog: bool qui dit que le mode débogage a été activé: pour la fin de partie
sortie: 
    ActivationDebog: tenir updaté le programme principale de l'activation (variable local vs globale)

fonctionOpenCSV: ouvrir un fichier csv et stocker son contenu 
entrée: nom du fichier 'exemple.csv' (String)
sortie: variable avec le contenu (liste 1,2,3 ou ...n dimensions je crois dépendant du nombre de colonnes)

fonctionOpenJSON: ouvrir un fichier json et stocker son contenu 
entrée: nom du fichier 'exemple.json' (String)
sortie: variable avec le contenu (Dictionnaire)

fonctionSaveCSV: stocke dans un fichier csv un contenu 
entrées: 
    nom du fichier 'exemple.csv' (String)
    variable avec contenu organisé à stocker (liste)
sortie: aucune (ou bool réussit ou non)

fonctionSaveJSON: stocke dans un fichier json un contenu
entrées: 
    nom du fichier 'exemple.json' (String)
    variable avec contenu organisé à stocker (dictionnaire)
sortie: aucune (ou bool réussit ou non)

fonctionEnregistrerPartieEnCours: enregistre la partie en cours dans un csv ou json à voir
entrées: tout ce qui constitue les infos d'une partie + pseudo 
sorties: aucune

fonctionFinDePartie: enregistrer le score et pseudo dans un csv (ou json)
entrées: 
    score (int)
    pseudo (String)
sorties: aucune
"""

""" TEST COLORAMA:

init()
print(Fore.RED + Style.NORMAL + 'Un texte rouge')
print(Back.BLACK + 'Avec un fond noir')
print(Style.BRIGHT + 'Plus lumineux !')
print(Style.RESET_ALL + 'Retour à la normale')
deinit()
"""

"""test readchar
def ReadClavierAcceuil():
#tant que enter ou "q" n'est pas cliqué on continue à lire les touches du clavier
#si l'une d'entre elle est cliquée on lance la fonction associée (ouvrir le menu ou alors quitter)
    while True: 
      keyPressed = readkey() #lit le clavier
      if keyPressed == key.ENTER:
        fonction2()
        break
      if keyPressed == "q":
        fonctionQuitter()
        break  
#en modifiant les touches on peut créer une fonction pour le mouvement du joueur:  ‘i’, ‘j’, ‘k’ et ‘l’ ou 
#touches 8 (haut), 4 (gauche), 5 et 2 (bas), et 6 (droite)
# exemple: if keyPressed == "i" or keyPressed == "8" ... 
"""