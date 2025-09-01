#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule la factorielle d'un nombre donné en utilisant la récursion.
    
    La factorielle d'un entier positif ou nul n est le produit de tous les 
    entiers positifs inférieurs ou égaux à n. Par définition, 0! = 1.
    
    Paramètres:
    -----------
    n : int
        Un entier positif ou nul pour lequel calculer la factorielle.
        Doit être >= 0.
    
    Retourne:
    ---------
    int
        La factorielle de n (n!). Retourne 1 si n est égal à 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Vérification qu'un argument a été fourni
if len(sys.argv) != 2:
    print("Usage: ./factorial_recursive.py <nombre>")
    print("Exemple: ./factorial_recursive.py 5")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    if n < 0:
        print("Erreur: Veuillez entrer un nombre positif ou nul")
        sys.exit(1)
    f = factorial(n)
    print(f)
except ValueError:
    print("Erreur: Veuillez entrer un nombre entier valide")
    sys.exit(1)
