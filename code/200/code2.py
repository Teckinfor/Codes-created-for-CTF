tableau = []
largeur = []
example = []
i = 0
j = 0
while i < 400 :
    largeur.append(example)
    i += 1

while j < 400 :
    tableau.append(largeur)
    j += 1

# Sauvegarde les pièces
piece = []
pieces = []
with open('puzzle.txt') as fic :
    for morceaux in fic :
        piece = morceaux[0:-1].split(" ")
        pieces.append(piece)

tableau[199][199] = pieces[0]

poubelle = []
First = True

#Resolution
while pieces or First:
    First = False
    c = 0
    for piece in pieces :
        if c % 5000 == 0 :
            print(str(c) + "/" + str(len(pieces)))
        c += 1
        match = False
        for cote in piece :
            #print(cote)
            i = 0
            j = 0
            while i < len(tableau) - 1:
                while j < len(tableau[i]) - 1:
                    if cote in tableau[i][j] :

                        if cote == tableau[i][j][0] :
                            tableau[i-1][j] = piece
                            match = True
                            break

                        if cote == tableau[i][j][1] :
                            tableau[i+1][j] = piece
                            match = True
                            break

                        if cote == tableau[i][j][2] :
                            tableau[i][j-1] = piece
                            match = True
                            break

                        if cote == tableau[i][j][3] :
                            tableau[i][j+1] = piece
                            match = True
                            break
                        
                    j += 1
                i += 1

        if not match:
            poubelle.append(piece)

    del pieces
    pieces = poubelle.copy()
    del poubelle
    poubelle = []
    
    #print(len(poubelle),len(pieces))

for ligne in tableau :
    for piece in ligne :
        print(piece[4], end="")

input()