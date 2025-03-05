def caseJouable(grille, coord, vide, joueur, joueurAdv):
	"""
	On regarde si la case de coordonnées coord, appartenant à joueur est une case jouable.
	C'est-à-dire, une case vide qui permet de retourner des pions adverses.

	La méthode pour rechercher si une case est jouable est très similaire à la fonction maj dans Othello.

	Attention, il n'es tplus possible ici d'utiliser l'astuce joueur%2+1 car je me trouve ici dans un module 
		qui pourraît être utilisé par un autre moteur de jeu que le mien. Donc la valeur des pions blancs, 
		noirs et de joueur peut etre différent.
	"""
	if grille[coord[0]][coord[1]] != vide:
		return False

	#descend
	prisePotentiel = []
	for i in range(coord[0]+1, 8):
		if grille[i][coord[1]] == joueurAdv:
			prisePotentiel.append((i, coord[1]))
		elif grille[i][coord[1]] == joueur and len(prisePotentiel) != 0:
			return True
		else:
			break

	#monte
	prisePotentiel = []
	for i in range(coord[0]-1, -1, -1):
		if grille[i][coord[1]] == joueurAdv:
			prisePotentiel.append((i, coord[1]))
		elif grille[i][coord[1]] == joueur and len(prisePotentiel) != 0:
			return True
		else:
			break

	#droite, grille
	prisePotentiel = []
	for j in range(coord[1]+1, 8):
		if grille[coord[0]][j] == joueurAdv:
			prisePotentiel.append((coord[0], j))
		elif grille[coord[0]][j] == joueur and len(prisePotentiel) != 0:
			return True
		else:
			break

	#gauche
	prisePotentiel = []
	for j in range(coord[1]-1, -1, -1):
		if grille[coord[0]][j] == joueurAdv:
			prisePotentiel.append((coord[0], j))
		elif grille[coord[0]][j] == joueur and len(prisePotentiel) != 0:
			return True
		else:
			break

	#diag bas-droite
	j=1
	prisePotentiel = []
	for i in range(coord[0]+1, 8):
		if i > 7 or coord[1]+j > 7:
			break
		if grille[i][coord[1]+j] == joueurAdv:
			prisePotentiel.append((i, coord[1]+j))
		elif grille[i][coord[1]+j] == joueur and len(prisePotentiel) != 0:
			return True
		else:
			break
		j+=1
	
	#diag bas-gauche
	j=1
	prisePotentiel = []
	for i in range(coord[0]+1, 8):
		if i > 7 or coord[1]-j < 0:
			break
		if grille[i][coord[1]-j] == joueurAdv:
			prisePotentiel.append((i, coord[1]-j))
		elif grille[i][coord[1]-j] == joueur and len(prisePotentiel) != 0:
			return True
		else:
			break
		j+=1

	#diag haut-droite
	i=1
	prisePotentiel = []
	for j in range(coord[1]+1, 8):
		if j > 7 or coord[0]-i < 0:
			break
		if grille[coord[0]-i][j] == joueurAdv:
			prisePotentiel.append((coord[0]-i, j))
		elif grille[coord[0]-i][j] == joueur and len(prisePotentiel) != 0:
			return True
		else:
			break
		i+=1

	#diag haut-gauche
	i=1
	prisePotentiel = []
	for j in range(coord[1]-1, -1, -1):
		if j < 0 or coord[0]-i < 0:
			break
		if grille[coord[0]-i][j] == joueurAdv:
			prisePotentiel.append((coord[0]-i, j))
		elif grille[coord[0]-i][j] == joueur and len(prisePotentiel) != 0:
			return True
		else:
			break
		i+=1

	return False

def trouverCoupsPossibles(grille, vide, joueur, joueurAdv):
	"""
	On parcours toutes les grilles de jeu et on teste case par case si elle est un coup possiblepour le joueur joueur.
	"""
	coupsPossibles = []

	for i in range(0,8):
		for j in range(0,8):
			if caseJouable(grille, (i,j), vide, joueur, joueurAdv):
				coupsPossibles.append((i,j))

	return coupsPossibles 
