""""
Exemple de module contenant des variables et des fonctions
"""
#Exemples de constantes
PRENOM = "Abdoul"
NOM = "FALL"
PI = 3.14

# définition de quelques variables
age = 25
message = "Salut les gars !"

#Définition de quelques fonctions
def calcul(a,b):
    """
    Per de d'additionner deux nombres entiers
    """
    return a + b

def bissextile(annee):
    """
    Permet de vérifier si une année est bissextile
    """
    return ((annee % 400 ) or ((annee % 4) and annee % 100 != 0))
              
          
if __name__=="__main__":
       resultat = calcul(2,5)
       print(resultat)
       print(annee_bissextile(2020))  
             
