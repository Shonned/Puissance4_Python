
# __________________ _BASIC__________________
# - Author: Shonned
# - Version: 1.0.0
# - https://github.com/Shonned/

# ====================== IMPORT ======================
import time
from random import randint
import secrets
import datetime

# __________________ _INIT__________________

echoDate = datetime.datetime.now()
echoDate = echoDate.strftime("%d/%m/%Y")
NB_LIGNES = randint(4, 10)
NB_COLONNES = randint(4, 10)
A = [['.' for j in range(NB_COLONNES)] for i in range(NB_LIGNES)]
isGameFinish = 0
n = NB_LIGNES * NB_COLONNES - 3

# __________________ _FONCTIONS __________________

def afficherJeu():
  for lignes in range (NB_LIGNES):
    for colonnes in range (NB_COLONNES):
      print(A[lignes][colonnes], end = " ")
    print()

def colonnesDispo(): # Affiche les indices des colonnes du plateau
  print ("["+ echoDate +"] >>> Colonnes disponibles:\n")
  for i in range(NB_COLONNES):
    print(i, end=' ')
  print('\n')
  afficherJeu()
  print('\n')

def verifierLignes(): # Vérifie si 4 pions sont alignés sur une ligne
  global isGameFinish
  for lignes in range (NB_LIGNES):
    compteurLignes = 0
    for colonnes in range (NB_COLONNES-1):
      if (A[lignes][colonnes] == A[lignes][colonnes+1]) and A[lignes][colonnes] !='.':
        compteurLignes += 1
        if compteurLignes == 3:
          print("["+ echoDate +"] >>> Le joueur " + player + ' a gagné')
          isGameFinish = 1 # La partie est fini
          break
      else:
        compteurLignes = 0

def verifierColonnes(): # Vérifie si 4 pions sont alignés sur une colonne
  global isGameFinish
  for colonnes in range (NB_COLONNES):
    compteurColonnes = 0
    for lignes in range (NB_LIGNES-1):
      if (A[lignes][colonnes] == A[lignes+1][colonnes]) and A[lignes][colonnes] != '.':
        compteurColonnes += 1
        if compteurColonnes == 3:
          print("["+ echoDate +"] >>> Le joueur " + player + ' a gagné')
          isGameFinish = 1 # La partie est fini
          break
      else:
        compteurColonnes = 0

def diagGaucheADroite(i, j):  # Vérifie si une diagonale existe de gacuhe à droite
  if A[i][j] != 'J' and A[i][j] != 'R':
    return False
  for k in range(1, 4):
    if i-k >= NB_LIGNES:
      return False
  for k in range(1, 4):
    if j+k >= NB_COLONNES:
      return False
  for k in range(1, 4):
    if A[i-k][j+k] != A[i][j]:
      return False
  return True

def diagDroiteAGauche(i, j): # Vérifie si une diagonale existe de droite à gauche
  if A[i][j] != 'J' and A[i][j] != 'R':
    return False
  for k in range(1, 4):
    if i-k >= NB_LIGNES:
      return False
  for k in range(1, 4):
    if j-k >= NB_COLONNES:
      return False
  for k in range(1, 4):
    if A[i-k][j-k] != A[i][j]:
      return False
  return True


def verifierCellule(): # Verifie si une diagonale est présente
  global isGameFinish
  for colonnes in range (NB_COLONNES):
    for lignes in range (NB_LIGNES):
      if diagGaucheADroite(lignes, colonnes) == True:
        isGameFinish = 1 # La partie est fini
        return True 
      if diagDroiteAGauche(lignes, colonnes) == True:
        isGameFinish = 1 # La partie est fini
        return True 
  return False
      

def ajouterPion(colonne, player): # Ajoute le pion selon la colonne choisit et le joueur
  global maLigne
  for i in range (NB_LIGNES-1, -1, -1):
    if A[i][colonne]  == '.':
      A[i][colonne] = player
      maLigne = i
      break

# __________________ _MAIN __________________

print("["+ echoDate +"] >>> Bienvenue sur « Rangée de 4 »\n")
print("["+ echoDate +"] >>> Un plateau aléatoire se génère...\n")
time.sleep(2) # Attendre 2 secondes

# ====== COLONNES ======

colonnesDispo()

# ====== MODE DE JEU ======
gameMode = input(">>> Mode de jeu disponibles: [PLAYERVSBOT (1) / PLAYERVSPLAYER (2)] ")
if gameMode != '1' and gameMode != '2':
  print('Une erreur est survenue')
  exit()
else:
  print('>>> Mode de jeu: ' + gameMode)

# NOTE: 2 Modes de jeu sont présents, PVP, PVB, c'est au joueur de choisir
# -> Renvoie une érreur si le mode de jeu n'existe pas.

# ====== NOM DU JOUEUR ======

if(gameMode == '1'): # Si le mode de jeu est PVB
  playerName = input(">>> Avant de commencer, comment t'appelles-tu ? ")
  playerName = ['POIL DE FESSE', 'CACA MOU', 'PUE DU BEC', 'FACE DE PET', 'LOSER']
  playerName = secrets.choice(playerName)
  print("\n>>> Tu m'a dis que tu t'appelais " + playerName + "? Très bien")
  time.sleep(2)
#====== NOM DU ROBOT ======
  botName = ['Didier', 'Denis', 'Samuel', 'Guillaume', 'Louis']
  botName = secrets.choice(botName)
  print('\n>>> Vous allez jouer contre ' + botName)
  time.sleep(2)
else: # Si le mode de jeu est PVP
  playerName = input(">>> Nom du joueur 1: ")
  player2Name = input(">>> Nom du joueur 2: ")


# ====== QUI COMMENCE======

player = ['J', 'R'] 
player = secrets.choice(player) # On choisit si le joueur qui commece
if player == 'J':
  print('\n>>> ' + playerName + ' va commencer')
  time.sleep(2)
elif gameMode == '2' and player == 'R':
  print('\n>>> ' + player2Name + ' va commencer')
else:
  print('\n>>> ' + botName + ' va commencer')

# ====== JEU ======


for i in range(n):
  while isGameFinish == 0: # Tant que "isGameFinish" (la partie est-elle fini) = 0
    if player == 'J' and isGameFinish != 1:
      colonne = int(input("\n["+ playerName +"] >>> Quelle colonne voulez vous: "))
      if(A[0][colonne] != '.'): # Si le sommet d'une colonne n'est pas vide
        print("["+ playerName +"] >>> Impossible de joueur ici")
        afficherJeu()
        player = 'J' # Le joueur doit recommencer
      else: # Sinon
        ajouterPion(colonne, 'J') # On ajoute le pion sur la colonne que le joueur à choisit
        print("\n["+ playerName +"] >>> Vous avez choisi la colonne " + str(colonne))
        print("["+ playerName +"] >>> Le pion se place sur la ligne " + str(maLigne) + "\n")
        verifierLignes() # On Vérifie les lignes
        verifierColonnes() # On Vérifie les colonnes
        verifierCellule() # On Vérifie les diagonales
        afficherJeu() # On affiche le plateau
        player = 'R' # On passe au joueur suivant
    if player == 'R' and isGameFinish != 1:
      if gameMode == '2': # Boucle si le mode de jeu est PVP
        print("\n["+ player2Name +"] >>> "+ player2Name +" va jouer...")
        colonne = int(input("\n["+ player2Name +"] >>> Quelle colonne voulez vous: "))
        print("\n["+ player2Name +"] >>> "+ player2Name +" a choisit la colonne " + str(colonne) + "\n")
        if(A[0][colonne] != '.'):
          print("["+ player2Name +"] >>> Impossible de joueur ici")
          player = 'R'
        else:
          ajouterPion(colonne, 'R')
          print("\n["+ player2Name +"] >>> Vous avez choisi la colonne: " + str(colonne))
          print("["+ player2Name +"] >>> Le pion se place sur la ligne " + str(maLigne) + "\n")
          verifierLignes()
          verifierColonnes()
          verifierCellule()
          afficherJeu()
          player = 'J'
      else: # Boucle si le mode de jeu est PVB
        time.sleep(2)
        print("\n["+ botName +"] >>> "+ botName +" va jouer...")
        colonne = randint(0, NB_COLONNES-1)
        time.sleep(2)
        print("\n["+ botName +"] >>> "+ botName +" a choisit la colonne " + str(colonne) + "\n")
        if(A[0][colonne] != '.'):
          print("["+ botName +"] >>> Impossible de joueur ici")
          player = 'R'
        else:
          ajouterPion(colonne, 'R')
          print("\n["+ botName +"] >>> Colonne alléatoire: " + str(colonne))
          print("["+ botName +"] >>> Le pion se place sur la ligne " + str(maLigne) + "\n")
          verifierLignes()
          verifierColonnes()
          verifierCellule()
          afficherJeu()
          player = 'J'
  else: # Si la partie est fini on affiche les messages
    print("["+ echoDate +"] >>> Partie fini, un joueur a gagné")
    print("["+ echoDate +"] >>> Relancez le script pour recommencer")

# ====== FIN ======
print("["+ echoDate +"] >>> Partie fini")

# __________________ _MAIN __________________
