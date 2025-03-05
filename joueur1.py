import generalJoueur as utile

nom = "joueur1"


def choix(grille, blanc, noir, vide, joueur, joueurAdv):
	coupEstValide = False
	i = -1
	j = -1
	#On fait une liste des coups possibles
	coupsPossibles = utile.trouverCoupsPossibles(grille, vide, joueur, joueurAdv)
	print("Coups possibles:",coupsPossibles)	

	#S'il n'y a aucun coup possible, on retourne none.
	if len(coupsPossibles) == 0:
		return None

	#tant que les coordonnées saisies par l'utilisateur ne se trouvent pas dans les coups possibles, on ressaisie.
	while (i, j) not in coupsPossibles: 
		#Les mots clés try et except sont nouveaux. On les utilise pour gérer ce que l'on appelle les exceptions.
		#Les exceptions sont des erreurs que l'on ne peut pas vérifier facilement avant que le programme soit lancé.
		#Ici par exemple, on veut caster (changer le type) la valeur saisie de string vers int. Mais si la valeur 
		#saisie n'est pas "castable" (par exemple je rentre un 'e', il ne sera pas possible de changer son type en int)
		#alors il va y avoir une erreur et notre programma va s'arreter. Pour éviter cela, on encadre les lignes
		#où peut se trouver cette erreur (ici les deux lignes de caste) entre try (c'est le début) et except 
		#(c'est la fin). À côté de except on dit que, si dans les lignes encadrées il y a une erreur de type 
		#ValueErreur (ce qui correspond à l'erreur de caste impossible) on continue le programme. Ici, on continue 
		#de tourner dans le boucle while.
		try:
			i = int(input("Saisissez numéro de ligne: "))-1
			j = int(input("Saisissez numéro de colone: "))-1
		except ValueError:
			pass
		

	return (i,j)


	


	



