"""
Test des exceptions Python
"""
def recherche_valeur_liste (liste, valeur):
    try:
        index = liste.index(valeur)
    except ValueError:
        index = "Valeur non trouvée dans la liste"
        return index
    else:
        return index

if __name__=="__main__":
    my_list = ["Pain", "Riz"]
    reponse = recherche_valeur_liste(my_list, "Orange")
    print(reponse)
