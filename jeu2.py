
import readchar
from readchar import readkey, key
import os
import json
import csv
from colorama import Back, Fore, Style, deinit, init
from random import randint
import random


#Fonction grille
def initialiser_grille():
    tailleGrillei = random.randint(9, 19)

    tailleGrillej = random.randint(19, 39)
    GrilleJoueur = [["X"] * (tailleGrillej) for _ in range(tailleGrillei)]
    positionJoueur = [random.randint(0,tailleGrillei-1), random.randint(0,tailleGrillej-1)]
    GrilleJoueur[positionJoueur[0]][positionJoueur[1]] = "J" #on place le joueur
    GrilleV1 = [[""] * tailleGrillej for _ in range(tailleGrillei)]
    GrilleV1[random.randint(0,tailleGrillei-1)][random.randint(0,tailleGrillej-1)] = "J" #on place le joueur
    tailleSituation = int(0.025*tailleGrillej*tailleGrillei)
    tailleMur = int(0.1*tailleGrillej*tailleGrillei)
    for i in range(tailleSituation): #positifs
        while True:
            chiffreX = random.randint(0,tailleGrillei-1)
            chiffreY = random.randint(0,tailleGrillej-1)
            if GrilleV1[chiffreX][chiffreY] == "":
                GrilleV1[chiffreX][chiffreY] = "P"
                break
    for i in range(tailleSituation): #negatifs
        while True:
            chiffreX = random.randint(0,tailleGrillei-1)
            chiffreY = random.randint(0,tailleGrillej-1)
            if GrilleV1[chiffreX][chiffreY] == "":
                GrilleV1[chiffreX][chiffreY] = "N"
                break
    for i in range(tailleMur): #negatifs
        while True:
            chiffreX = random.randint(0,tailleGrillei-1)
            chiffreY = random.randint(0,tailleGrillej-1)
            if GrilleV1[chiffreX][chiffreY] == "":
                GrilleV1[chiffreX][chiffreY] = "M"
                break
    while True:
        chiffreX = random.randint(0, tailleGrillei-1)
        chiffreY = random.randint(0, tailleGrillej-1)
        if GrilleV1[chiffreX][chiffreY] == "":
            GrilleV1[chiffreX][chiffreY] = "S"
            break
    return GrilleJoueur, GrilleV1, positionJoueur, tailleGrillei-1, tailleGrillej-1


def afficher_grille(ma_grille):
    print("┌" + "───┬" * (len(ma_grille[0]) - 1) + "───┐")
    for i, ligne in enumerate(ma_grille):
        if i != 0:
            print("├" + "───┼" * (len(ligne) - 1) + "───┤")
        for valeur in ligne:
            print("│ " + valeur + " ", end="")

        print("│")
    print("└" + "───┴" * (len(ligne) - 1) + "───┘")

def afficher_accueil():
    print("Bienvenue dans le jeu !")
    print("Le jeu le plus amusant de tous les temps !")
    print("Créé par Ines et Albane en 2024")
    input("Appuyez sur Entrée pour continuer...")

def afficher_menu():
    print("Menu principal :")
    print("1. Jouer")
    print("2. Voir les règles")
    print("3. Quitter")
    choix = input("Entrez votre choix : ")
    return choix

def afficher_regles():
    print("Règles du jeu :")
    # Ajouter ici les règles du jeu
    input("Appuyez sur Entrée pour revenir au menu principal...")

def afficher_jeu():

    print("Save the Fish!")
    print("Légende des cases")
    print("Grille de jeu")
    grilleJ, GrilleAdmin, posJoueur, tailleI, tailleJ = initialiser_grille()
    afficher_grille(grilleJ)
    print("Score actuel : [score]")
    print("Indications pour le joueur")
    print("afficher jeu")
    return grilleJ, GrilleAdmin, posJoueur, tailleI, tailleJ

def handle_player_movement(player_position, orientation, grilleAdminF, grilleJoueurF, tailleIF,tailleJF):
    while True:
        print("inwhile")
        key_pressed = readchar.readkey()
        print(key_pressed)
        print("ok")
        if (key_pressed == "i" or key_pressed == "8") and orientation == "i" and player_position[0] > 0 :
            if grilleAdminF[player_position[0]-1][player_position[1]] == "M":
                print("Attention un mur")
            else:
                player_position = [player_position[0]-1, player_position[1]]
                break
        elif (key_pressed == "j" or key_pressed == "4")and orientation == "j" and player_position[1] > 0:
            if grilleAdminF[player_position[0]][player_position[1]-1] == "M":
                print("Attention un mur")
            else:
                player_position = [player_position[0], player_position[1]-1]
                break
        elif (key_pressed == "k" or key_pressed == "5" or key_pressed == "2") and orientation == "k" and player_position[0] < tailleIF:
            if grilleAdminF[player_position[0]+1][player_position[1]] == "M":
                print("Attention un mur")
            else:
                player_position = [player_position[0]+1, player_position[1]]
                break
        elif (key_pressed == "l" or key_pressed == "6") and orientation == "l" and player_position[0] < tailleJF:
            if grilleAdminF[player_position[0]][player_position[1]+1] == "M":
                print("Attention un mur")
            else:
                player_position = [player_position[0], player_position[1]+1]
                break
        elif key_pressed == "i":
            orientation = "i"
            if grilleAdminF[player_position[0]-1][player_position[1]] == "P" or grilleAdminF[player_position[0]-1][player_position[1]] == "N" :
                #change la couleur du joueur
                print("attention, vou etes en face d'une situation")
        elif key_pressed == "j":
            orientation = "j"
            if grilleAdminF[player_position[0]][player_position[1]-1] == "P" or grilleAdminF[player_position[0]][player_position[1]-1] == "N":
                # change la couleur du joueur
                print("attention, vou etes en face d'une situation")
        elif key_pressed == "k":
            orientation = "k"
            if grilleAdminF[player_position[0]+1][player_position[1]] == "P" or grilleAdminF[player_position[0]+1][player_position[1]] == "N":
                # change la couleur du joueur
                print("attention, vou etes en face d'une situation")
        elif key_pressed == "l":
            orientation = "l"
            if grilleAdminF[player_position[0]][player_position[1]+1] == "P" or grilleAdminF[player_position[0]][player_position[1]+1] == "N":
                # change la couleur du joueur
                print("attention, vou etes en face d'une situation")
    print("outwhile")
    return player_position, orientation


#FONCTIONS STOCKAGE

#fonctionOpenCSV: ouvrir un fichier csv et stocker son contenu
    #entrée: nom du fichier 'exemple.csv' (String)
    #sortie: variable avec le contenu (liste 1,2,3 ou ...n dimensions je crois dépendant du nombre de colonnes)
import csv

def fonction_open_csv(nom_fichier):
    contenu = []
    with open(nom_fichier, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            contenu.append(row)
    return contenu
## appel : contenu = fonction_open_csv('exemple.csv')

#fonctionOpenJSON: ouvrir un fichier json et stocker son contenu
    #entrée: nom du fichier 'exemple.json' (String)
    #sortie: variable avec le contenu (Dictionnaire)
import json

def fonction_open_json(nom_fichier):
    with open(nom_fichier, 'r') as json_file:
        contenu = json.load(json_file)
    return contenu
## appel : contenu = fonction_open_json('exemple.json')

#fonctionSaveCSV: stocke dans un fichier csv un contenu
    #entrées:
    # nom du fichier 'exemple.csv' (String)
    # variable avec contenu organisé à stocker (liste)
    #sortie: aucune (ou bool réussit ou non)

import csv

def fonction_save_csv(nom_fichier, contenu):
    try:
        with open(nom_fichier, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in contenu:
                writer.writerow(row)
        return True  # Succès de l'écriture dans le fichier
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return False  # Échec de l'écriture dans le fichier

def fonction_save_json(nom_fichier, contenu):
    try:
        with open(nom_fichier, 'w') as json_file:
            json.dump(contenu, json_file, indent=4)
        return True  # Succès de l'écriture dans le fichier
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return False  # Échec de l'écriture dans le fichier

def SelectionChoix(choix):
    while True:
        if choix == "1":
            grilleJ2, GrilleAdmin2, posJoueur2, tailleI1, tailleJ1 = afficher_jeu()
            print("selectionchoix")
            return grilleJ2, GrilleAdmin2, posJoueur2, tailleI1, tailleJ1

        elif choix == "2":
            afficher_regles()
            break
        elif choix == "3":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def fonctionPrincipale():
    afficher_accueil()
    choixP =afficher_menu()
    grilleJoueurG, GrilleAdminG, posJoueurG, tailleIG, tailleJG = SelectionChoix(choixP)
    orientationG = "" #par défaut orienté vers le haut
    print("ok")
    posJoueurG, orientationG = handle_player_movement(posJoueurG, orientationG, GrilleAdminG, grilleJoueurG, tailleIG,tailleJG )
    afficher_grille(GrilleAdminG)

fonctionPrincipale()