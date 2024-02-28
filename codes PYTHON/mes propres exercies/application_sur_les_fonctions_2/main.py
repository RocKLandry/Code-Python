'''Dans cet exercice on va imbriquer des fonctions et surtout utliser des fonctions qui vont retourner
plusieurs valeurs'''

def majorite(age):
    if age>=18:
        print("la personne est majeure")
    else:
        print("La personne n'est pas majeure")

def recuperer_info_personne(numero_personne):
    nom=input(" Quel est le nom de la personne " + str(numero_personne) + " ? ")
    age=input(" Quel est l'age de la personne" + str(numero_personne) + " ? ")
    return nom,age


def afficher_info_personne(numero_personne,nom_personne,age_personne):
    print("La personne numero",numero_personne,"est",nom_personne,"son age est :",age_personne," ans")
    print("le nom comporte",len(nom_personne),"caracteres")

def recuperer_et_afficher_info_personne(numero_personne):
    nom,age=recuperer_info_personne(numero_personne)
    afficher_info_personne(numero_personne, nom,age)
    majorite(int(age))

''' Toute fois on pourra utiliser les boucles et les conditions et tests pour
ameliorer notre code, le rendre fiable et securiser les donnes saisies'''

recuperer_et_afficher_info_personne(1)