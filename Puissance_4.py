noms = []
scores = [0,0]
def saisir_nom_2_joueurs():
    joueur1 = input("Entrer le nom du joueur 1 : ")
    noms.append(joueur1)
    joueur2 = input("Entrer le nom du joueur 2 : ")
    noms.append(joueur2)
def init_grille():
    rows = 6
    cols = 7
    grill = [[" " for _ in range(cols)] for _ in range(rows)]
    return grill
def afficher_grille(grille):
    i = 0
    print("  0 1 2 3 4 5 6")
    for row in grille:
        print(i,end=" ")
        print(" ".join(row))
        i += 1

def saisir_colonne_joueur_actif(noms,player):
    col = int(input(f"{noms[int(player)]}, choose a column (0-6): "))
    return col

def mette_a_jour_grille(grille,col,player):
    for i in range(5, -1, -1):
        if grille[i][col] == " ":
            grille[i][col] = player
            break
    return grille
def partie_finie(grille, player):
    # Check horizontally
    for row in grille:
        for i in range(len(row) - 3):
            if all(cell == player for cell in row[i:i+4]):
                return True

    # Check vertically
    for col in range(len(grille[0])):
        for i in range(len(grille) - 3):
            if all(grille[row][col] == player for row in range(i, i+4)):
                return True

    # Check diagonally (from top-left to bottom-right)
    for row in range(len(grille) - 3):
        for col in range(len(grille[0]) - 3):
            if all(grille[row+i][col+i] == player for i in range(4)):
                return True

    # Check diagonally (from top-right to bottom-left)
    for row in range(len(grille) - 3):
        for col in range(3, len(grille[0])):
            if all(grille[row+i][col-i] == player for i in range(4)):
                return True
    return False
def init_scores_du_joueur_actif(player):
    if player == '0':
        scores[0] += 1
    else:
        scores[1] += 1
    return scores
def affiche_pat(grille):
    for row in grille:
        if " " in row:
            return False
    return True

def changer_joueur_actif(player):
    player = "0" if player == "1" else "1"
    return player

def afficher_scores():
    print(f"Score du {noms[0]} : ", scores[0])
    print(f"Score du {noms[1]} : ", scores[1])

def demander_nouvelle_partie():
    choix = int(input("1) Nouvelle partie \n2) Sortie \nSaisissez un nombre : "))
    if choix == 1:
        return True
    else:
        return False
def joue():
    grille = init_grille()
    player = "0"
    while True:
        afficher_grille(grille)
        column = saisir_colonne_joueur_actif(noms,player)
        grille = mette_a_jour_grille(grille,column,player)
        # Check if the column is valid
        if 0 <= column < 7 and grille[0][column] == " ":
            if partie_finie(grille, player):
                afficher_grille(grille)
                init_scores_du_joueur_actif(player)
                print(f"{noms[int(player)]}, vous avez gagné...")
                break
            elif affiche_pat(grille):
                afficher_grille(grille)
                print("La partie est nulle.")
                break

            # Switch players
            player = changer_joueur_actif(player)
        else:
            print("Invalid move. Please choose a valid column.")


if __name__ == "__main__":
    saisir_nom_2_joueurs()
    while True:
        choix = demander_nouvelle_partie()
        if choix:
            joue()
            afficher_scores()
        else:
            print("Thank you for playing the game.")
            break
