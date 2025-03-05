import joueur1 as j1
import joueur2 as j2

def afficher(g):
	"""
	Affichage du plateau de jeu.
	"""
	numerosHorizontaux = "   "
	for i in range(1, 9):
		numerosHorizontaux += str(i)+" "

	print(numerosHorizontaux+"\n")
	for i in range(0, 8):
		ligne = str(i+1)+"  "
		for j in range(0,8):
			if g[i][j] != 0:
				ligne += str(g[i][j]) + " "
			else:
				ligne += "- "
		print(ligne, (i+1))
	print("\n"+numerosHorizontaux)

def retourne(prisePotentiel, grille):
	"""
	Permet de retourner les pions de la liste prisePotentiel dans la couleur adverse.
	Cette fonction ne retourne que dans une direction.
	Le paramètre prisePotentiel doit donc seulement contenir des pions de la mêmes couleurs, 
		contigüs sur le plateau et dans une seule direction.
	"""
	#[(4,4),(5,4),(6,4)]
	for i in range(0, len(prisePotentiel)):
		grille[prisePotentiel[i][0]][prisePotentiel[i][1]] = grille[prisePotentiel[i][0]][prisePotentiel[i][1]]%2+1
	return grille

def maj(grille, joueur, coord):
	"""
	À partir de l'emplacement coord (qui sont les coordonnées du pion qui vient être joué), vérifie dans les 8 directions possibles s'il y a des pions à retourner.
	Les recherches dans les 8 directions ont la même structure :

	prisePotentiel = []
	for i in range(coord[0]+1, 8):						#On part de coord+1 et on ira potentiellement jusqu'à 8.
		if grille[i][coord[1]] == joueur%2+1:			#Si la case que l'on croise est un pion adverse
			prisePotentiel.append((i, coord[1]))			#Alors on ajoute les coordonnées de cette case à la liste de PrisePotentiel
		elif grille[i][coord[1]] == joueur:				#Sinon si la case que l'on croise est un pion appartenant ou joueur qui vient de poser
			grille = retourne(prisePotentiel, grille)		#Alors on retourne les prisePotentiel. Si prisePotentiel est vide, il ne se passera rien.
			break											#On arrête de chercher des pions dans cette direction
		else:											#Sinon (C'est-à-dire si l'on rencontre un bord ou une case vide)
			break											#On arrête de chercher des pions car aucun ne sera à retourner.
	"""
	
	#On oublie de commencer par mettre à jour la case qui vient d'ere jouée.
	grille[coord[0]][coord[1]] = joueur
	
	#descend
	prisePotentiel = []
	for i in range(coord[0]+1, 8):
		if grille[i][coord[1]] == joueur%2+1:
			prisePotentiel.append((i, coord[1]))
		elif grille[i][coord[1]] == joueur:
			grille = retourne(prisePotentiel, grille)
			break
		else:
			break

	#monte
	prisePotentiel = []
	for i in range(coord[0]-1, -1, -1):
		if grille[i][coord[1]] == joueur%2+1:
			prisePotentiel.append((i, coord[1]))
		elif grille[i][coord[1]] == joueur:
			grille = retourne(prisePotentiel, grille)
			break
		else:
			break

	#droite, grille
	prisePotentiel = []
	for j in range(coord[1]+1, 8):
		if grille[coord[0]][j] == joueur%2+1:
			prisePotentiel.append((coord[0], j))
		elif grille[coord[0]][j] == joueur:
			grille = retourne(prisePotentiel, grille)
			break
		else:
			break

	#gauche
	prisePotentiel = []
	for j in range(coord[1]-1, -1, -1):
		if grille[coord[0]][j] == joueur%2+1:
			prisePotentiel.append((coord[0], j))
		elif grille[coord[0]][j] == joueur:
			grille = retourne(prisePotentiel, grille)
			break
		else:
			break

	#diag bas-droite
	j=1
	prisePotentiel = []
	for i in range(coord[0]+1, 8):
		if i > 7 or coord[1]+j > 7:
			break
		if grille[i][coord[1]+j] == joueur%2+1:
			prisePotentiel.append((i, coord[1]+j))
		elif grille[i][coord[1]+j] == joueur:
			retourne(prisePotentiel, grille)
			break
		else:
			break
		j+=1
	
	#diag bas-gauche
	j=1
	prisePotentiel = []
	for i in range(coord[0]+1, 8):
		if i > 7 or coord[1]-j < 0:
			break
		if grille[i][coord[1]-j] == joueur%2+1:
			prisePotentiel.append((i, coord[1]-j))
		elif grille[i][coord[1]-j] == joueur:
			retourne(prisePotentiel, grille)
			break
		else:
			break
		j+=1

	#diag haut-droite
	i=1
	prisePotentiel = []
	for j in range(coord[1]+1, 8):
		if j > 7 or coord[0]-i < 0:
			break
		if grille[coord[0]-i][j] == joueur%2+1:
			prisePotentiel.append((coord[0]-i, j))
		elif grille[coord[0]-i][j] == joueur:
			retourne(prisePotentiel, grille)
			break
		else:
			break
		i+=1

	#diag haut-gauche
	i=1
	prisePotentiel = []
	for j in range(coord[1]-1, -1, -1):
		if j < 0 or coord[0]-i < 0:
			break
		if grille[coord[0]-i][j] == joueur%2+1:
			prisePotentiel.append((coord[0]-i, j))
		elif grille[coord[0]-i][j] == joueur:
			retourne(prisePotentiel, grille)
			break
		else:
			break
		i+=1


#Ce sont des constantes, donc on les mets en majuscule par convention.
#Nous choisissons de représenter les BLANC par des 1 et NOIR par des 2.
#Nous choisissons également d'utiliser une variable joueur pour savoir à qui est le tour. Cette variable vaudra 1 ou 2.
#Il sera ainsi possible de très facilement retourner des pions avec l'astuce joueur%2+1 utilisé à beaucoup d'endroits.
BLANC = 1
NOIR = 2
VIDE = 0


grille = [	[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 1, 2, 0, 0, 0],
			[0, 0, 0, 2, 1, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],]

joueur = 1
coord = None
tourPasse = 0
compteTours = 0
while compteTours < 60: #il y a maximum 60 tours de jeu
	afficher(grille)
	print()

	if joueur == 1:
		print("joueur", j1.nom ,"à toi")
		coord = j1.choix(grille, BLANC, NOIR, VIDE, BLANC, NOIR) #On demande au joueur 1 de faire un choix.
	else:
		print("joueur", j2.nom ,"à toi")
		coord = j2.choix(grille, BLANC, NOIR, VIDE, NOIR, BLANC) #OU on demande au joueur 2 de faire un choix.

	if coord != None: #Si le joueur peut jouer.
		maj(grille, joueur, coord) #On met à jour la grille
		tourPasse = 0
		compteTours += 1
	else:
		tourPasse+=1 #Sinon on compte que nous venons de passer un tour.

	if tourPasse == 2: #Si l'on vient de passer 2 tours, c'est que plus aucun joueur ne peut jouer
		break #on arrete le jeu

	joueur = joueur%2+ 1 #On change de joueur avec notre astuce
	#time.sleep(0.2) #Utile si ce sont des IA qui s'affronte et que l'on veut ce qui se passe.

#Affichage à la fin du jeu.
afficher(grille)

#On compte le nombre de pion pour définir le gagnant.
nbJ1 = 0
nbJ2 = 0
for i in range(0,8):
	for j in range(0,8):
		if grille[i][j] == 1:
			nbJ1 += 1
		elif grille[i][j] == 2:
			nbJ2 += 1

if nbJ2 > nbJ1:
	print("joueur", j2.nom,"a gagné : ", nbJ2,"/", nbJ1)
elif nbJ2 < nbJ1:
	print("joueur", j1.nom,"a gagné : ", nbJ1,"/", nbJ2)
else:
	print("égalité.")




