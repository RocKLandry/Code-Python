'''Dans cet exercice nous allons recuperer les noms des personnes et les stocker dans une liste
puis à la fin afficher tous les noms saisis'''

noms=[]
nom=" " # j'ai initialise nom avec un caractere espace pour rentrer dans la boucle
while nom!="":
    nom=input("Donner un nom, pour arreter la saisie validez sans ecrire un nom! : ")
    if nom=="":
        break # si on ne saisie rien on sort de la boucle

    noms.append(nom) # là on ajoute le nom dans la liste noms

''' 
on pouvais aussi utliser une boucle infinie genre
while True:
    nom=input("Donner un nom, pour arreter la saisie validez sans ecrire un nom!  ")
    if nom=="":
        break 
    noms.append(nom) 
'''


print("Les noms saisis sont:")
for i in noms:
    print("")
    print(i)
