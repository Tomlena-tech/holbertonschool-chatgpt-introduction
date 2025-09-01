#!/usr/bin/python3

def print_board(board):
    """
    Affiche le plateau de jeu de Tic-Tac-Toe.
    
    Affiche le plateau sous forme de grille 3x3 avec des séparateurs
    visuels entre les cases et les lignes.
    
    Paramètres:
    -----------
    board : list[list[str]]
        Matrice 3x3 représentant l'état actuel du plateau de jeu.
        Chaque case contient soit "X", "O", ou " " (espace vide).
    
    Retourne:
    ---------
    None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Vérifie s'il y a un gagnant sur le plateau de jeu.
    
    Contrôle toutes les conditions de victoire possibles :
    lignes, colonnes et diagonales.
    
    Paramètres:
    -----------
    board : list[list[str]]
        Matrice 3x3 représentant l'état actuel du plateau de jeu.
    
    Retourne:
    ---------
    bool
        True s'il y a un gagnant, False sinon.
    """
    # Vérification des lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True
    
    # Vérification des colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True
    
    # Vérification de la diagonale principale
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    
    # Vérification de la diagonale secondaire
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    
    return False

def is_board_full(board):
    """
    Vérifie si le plateau est complètement rempli.
    
    Parcourt toutes les cases pour déterminer s'il reste
    des cases vides disponibles.
    
    Paramètres:
    -----------
    board : list[list[str]]
        Matrice 3x3 représentant l'état actuel du plateau de jeu.
    
    Retourne:
    ---------
    bool
        True si le plateau est plein, False sinon.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Lance et gère une partie complète de Tic-Tac-Toe.
    
    Initialise le plateau, gère l'alternance des joueurs,
    traite les entrées utilisateur et détermine le gagnant
    ou déclare un match nul.
    
    Paramètres:
    -----------
    Aucun
    
    Retourne:
    ---------
    None
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while not check_winner(board) and not is_board_full(board):
        print_board(board)
        
        try:
            row = int(input("Entrez la ligne (0, 1, ou 2) pour le joueur " + player + ": "))
            col = int(input("Entrez la colonne (0, 1, ou 2) pour le joueur " + player + ": "))
            
            # Vérification que les coordonnées sont valides
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Coordonnées invalides ! Utilisez 0, 1, ou 2.")
                continue
            
            if board[row][col] == " ":
                board[row][col] = player
                # Alternance des joueurs
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("Cette case est déjà prise ! Essayez encore.")
                
        except ValueError:
            print("Veuillez entrer un nombre valide !")
        except IndexError:
            print("Coordonnées hors limites ! Utilisez 0, 1, ou 2.")
    
    print_board(board)
    
    # Détermination du résultat
    if check_winner(board):
        # Le joueur affiché est celui qui vient de jouer (avant l'alternance)
        winner = "O" if player == "X" else "X"
        print("Le joueur " + winner + " a gagné !")
    else:
        print("Match nul ! Le plateau est plein.")

if __name__ == "__main__":
    tic_tac_toe()
