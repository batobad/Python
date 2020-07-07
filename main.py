"""
Ce module est le point d'entré du programme
"""
import sys

from gestion_formation.controller import ajouter, afficher
from gestion_formation.view import menu

def main():
    menu()
    while True:
        choix = int(input("Votre choix: "))
        if choix == 1:
             valeur = input("Donnez un nom: ")
             ajouter(valeur)
        elif choix == 2:
            afficher()
        elif choix == 3:
            sys.exit()
        else:
            print("Choix inconnu")
   

if __name__=="__main__":
    main()
