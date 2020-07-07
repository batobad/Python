"""
Ce programme montre comment accéder aux elements d'une listes imbriquées
avec une seule boucle for. Chaque liste imbriquée contient les données
d'un étudiant donné: le prenom, le nom, l'adresse, le téléphone et l'e-mail
"""
liste_etudiants = [
                    ["Ibrahima", "Sow", "Castors", "77 586 69 85", "ibsow@gmail.com"],
                    ["Fatou", "Guisse", "HLM5", "70 586 69 85", "fguisse@gmail.com"],
                    ["Jean-Pierre", "Ngom", "Dakar plateau", "78 235 85 36", "jpngom@yahoo.com"]
                ]

"""
Parcours de la liste_etudiants et affichage des données
Ici nous utilisons une boucle for et l'affectation du contenu de chaque liste imbriquée
à plusieurs variables. Remarquez l'équilibre des deux côtés du signe égal est bien respecté
"""
PRENOM = "Prénom"
NOM = "Nom"
ADRESSE = "Adresse"
TEL = "Téléphone"
EMAIL = "E-mail"

print("Affichage des données de chaque étudiant")
print("=" * 80)
print("{0:15s} {1:15s} {2:15s} {3:15s} {4}".format(PRENOM,NOM,ADRESSE,TEL,EMAIL))
for etudiant in liste_etudiants:
    prenom, nom, adresse, tel, email = etudiant
    print(f"{prenom:16}{nom:16}{adresse:16}{tel:16}{email}")
    
    
