"""
Ce module est le point d'entrée de l'application
"""
import sys
import calculs
from annee_bissextile import bissextile

def menu():
    """Le menu principal de l'application """
    print("1 - Addition ")
    print("2 - Sosutraction ")
    print("3 - Multiplication ")
    print("4 - Division ")
    print("5 - Modulo ")
    print("6 - Aannée bissextile ")
    print("7 - Quitter ")


def main():
    """Fonction main"""
    menu()
    choix = int(input("Votre choix: "))
    if choix == 1:
        nombre1 = int(input("Donnez le premier nombre: "))
        nombre2 = int(input("Donnez le deuxième nombre: "))
        print(calculs.addition(nombre1, nombre2))
    elif choix == 2:
        nombre1 = int(input("Donnez le premier nombre: "))
        nombre2 = int(input("Donnez le deuxième nombre: "))
        print(calculs.sosutraction(nombre1, nombre2))
    elif choix == 3:
        nombre1 = int(input("Donnez le premier nombre: "))
        nombre2 = int(input("Donnez le deuxième nombre: "))
        print(calculs.multiplication(nombre1, nombre2))
    elif choix == 4:
        nombre1 = int(input("Donnez le premier nombre: "))
        nombre2 = int(input("Donnez le deuxième nombre: "))
        print(calculs.division(nombre1, nombre2))
    elif choix == 5:
        nombre1 = int(input("Donnez le premier nombre: "))
        nombre2 = int(input("Donnez le deuxième nombre: "))
        print(calculs.reste_division(nombre1, nombre2))
    elif choix == 6:
        annee = int(input("Donnez l'année: "))
        print(bissextile(annee))
    elif choix == 7:
        sys.exit()
    else:
        print("Opération incconue")

if __name__=="__main__":
    main()
        
