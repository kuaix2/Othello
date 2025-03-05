import generalJoueur as utile

nom = "joueur2"

# def afficher_temp(g):
# 	"""
# 	Affichage du plateau de jeu.
# 	"""
# 	numerosHorizontaux = "   "
# 	for i in range(1, 9):
# 		numerosHorizontaux += str(i)+" "

# 	print(numerosHorizontaux)
# 	for i in range(0, 8):
# 		ligne = str(i+1)+"  "
# 		for j in range(0,8):
# 			if g[i][j] != 0:
# 				ligne += str(g[i][j]) + " "
# 			else:
# 				ligne += "= "
# 		print(ligne, (i+1))


def retourne_temp(prisePotentiel, g):
	#[(4,4),(5,4),(6,4)]
	for i in range(0, len(prisePotentiel)):
		g[prisePotentiel[i][0]][prisePotentiel[i][1]] = g[prisePotentiel[i][0]][prisePotentiel[i][1]]%2+1
	return g

def maj_temp(g, joueur, coord):
	
	#On oublie de commencer par mettre à jour la case qui vient d'ere jouée.
	g[coord[0]][coord[1]] = joueur
	
	#descend
	prisePotentiel = []
	for i in range(coord[0]+1, 8):
		if g[i][coord[1]] == joueur%2+1:
			prisePotentiel.append((i, coord[1]))
		elif g[i][coord[1]] == joueur:
			g = retourne_temp(prisePotentiel, g)
			break
		else:
			break

	#monte
	prisePotentiel = []
	for i in range(coord[0]-1, -1, -1):
		if g[i][coord[1]] == joueur%2+1:
			prisePotentiel.append((i, coord[1]))
		elif g[i][coord[1]] == joueur:
			g = retourne_temp(prisePotentiel, g)
			break
		else:
			break

	#droite, g
	prisePotentiel = []
	for j in range(coord[1]+1, 8):
		if g[coord[0]][j] == joueur%2+1:
			prisePotentiel.append((coord[0], j))
		elif g[coord[0]][j] == joueur:
			g = retourne_temp(prisePotentiel, g)
			break
		else:
			break

	#gauche
	prisePotentiel = []
	for j in range(coord[1]-1, -1, -1):
		if g[coord[0]][j] == joueur%2+1:
			prisePotentiel.append((coord[0], j))
		elif g[coord[0]][j] == joueur:
			g = retourne_temp(prisePotentiel, g)
			break
		else:
			break

	#diag bas-droite
	j=1
	prisePotentiel = []
	for i in range(coord[0]+1, 8):
		if i > 7 or coord[1]+j > 7:
			break
		if g[i][coord[1]+j] == joueur%2+1:
			prisePotentiel.append((i, coord[1]+j))
		elif g[i][coord[1]+j] == joueur:
			g = retourne_temp(prisePotentiel, g)
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
		if g[i][coord[1]-j] == joueur%2+1:
			prisePotentiel.append((i, coord[1]-j))
		elif g[i][coord[1]-j] == joueur:
			g = retourne_temp(prisePotentiel, g)
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
		if g[coord[0]-i][j] == joueur%2+1:
			prisePotentiel.append((coord[0]-i, j))
		elif g[coord[0]-i][j] == joueur:
			g = retourne_temp(prisePotentiel, g)
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
		if g[coord[0]-i][j] == joueur%2+1:
			prisePotentiel.append((coord[0]-i, j))
		elif g[coord[0]-i][j] == joueur:
			retourne_temp(prisePotentiel, g)
			break
		else:
			break
		i+=1

	return g

def choix(grille, blanc, noir, vide, joueur, joueurAdv):
	
	coupsPossibles = utile.trouverCoupsPossibles(grille, vide, joueur, joueurAdv)
	print("Coups possibles:",coupsPossibles)

	#pas de coups possibles
	if len(coupsPossibles) == 0:
		return None

	
	for i in range(len(coupsPossibles)):
		coord=coupsPossibles[i]
		#4 corner
		if coord==(0,0) or coord==(0,7) or coord==(7,0) or coord==(7,7):
			print("jouer les coins",coord)
			return coord

		#border except for 12
		for i in range(2,6):
			for j in (0,7):
				if coord==(i,j):
					print("jouer les bords",coord)
					return coord
		for j in range(2,6):
			for i in (0,7):
				if coord==(i,j):
					print("jouer les bords",coord)
					return coord

 
	
	min_len=60
	bad_pos=[(1,1),(1,6),(6,1),(6,6)]
	for s in range(len(coupsPossibles)):

		coord_temp=coupsPossibles[s]
		g_temp=[[0]*8 for i in range(8)] #copy
		for i in range(0,8):
			for j in range(0,8):
				g_temp[i][j]=grille[i][j]	

		g_temp = maj_temp(g_temp, joueur, coord_temp)
		print("\n\nL'ordinateur a joué",coord_temp,"preview")
		# afficher_temp(g_temp)
		coupsPossibles_temp = utile.trouverCoupsPossibles(g_temp, vide, joueurAdv,joueur)
		len_temp=len(coupsPossibles_temp)

		print("coups possibles de l'adversaire",coupsPossibles_temp,"longueur",len_temp)

		if coord_temp in bad_pos: #si jouer position x
			len_temp=60

		if len_temp <= min_len: #l'adversaire mange le moin de pions possible
			min_len=len_temp
			coord=coord_temp

	print("\n\nAction final:",coord)

	return (coord)

	


	


	



