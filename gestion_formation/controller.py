"""
Le controlleur du projet
"""
from .model import my_list

def ajouter(element):
    """Permet d'ajouter des éléments dans la liste"""
    my_list.append(element)
    


def afficher():
    """Permet de parcourrir et d'afficher le contenu de my_list"""
    for i in my_list:
        print(i)