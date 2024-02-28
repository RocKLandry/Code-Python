''' dans cet exercice je vais definir des fonctions puis les appeler'''

def recuperer_et_afficher_info_personne(num_personne):

    nom=input("Quel est le nom de la personne numero " + str(num_personne) + " ? ")

    '''La fonction input n'a qu'un seul parametre qui est le message voilà pourquoi pour afficher
     une variable avec il faut concatener et j'ai du convertir num_personne car on concataine que
     des chaines avec des chaines '''

    age=input("quel est l'age de la per sonne numero " + str(num_personne) + " ? ")
    print("La personne numero",num_personne,"est ",nom,", et vous avez", age,"ans")
    print("Votre nom comporte",len(nom),"caracteres")

# Là je fais à present appel à ma fonction ! bon je vais l'appeler 3 fois c'est mon choix



'''
recuperer_et_afficher_info_personne(1)
recuperer_et_afficher_info_personne(2)
recuperer_et_afficher_info_personne(3)
'''

# à present on va utiliser une boucle pour ameliorer notre code ! on creera une variable nombre_personne
nombre_personne=int((input("Pour combien de personne voulez vous recuperer les infomations ?  ")))

for i in range(nombre_personne):
    recuperer_et_afficher_info_personne(i+1)
    ''' j'ai fourni le parametre i+1 pour que cela varie de 1,2 eet 3'''



'''
toute fois il faut savoir qu'on imbriquer des 
fonctions c'est à dire appeler des fonctions dans des fonctions
'''