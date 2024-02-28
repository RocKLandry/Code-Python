'''Dans cet exercice on va creer une liste qui contiendra des tuples dans lesquels on associera
le nom d'un livreur à sa distance

le programme doit renvoyer la distance du livreur le plus proche et son nom '''




#creation de la liste avec pour elements des tuples contenant des noms et distances des livreurs

livreurs_et_distance=[("ben",12.4),("rock",8.6),("michel",2.8),("steve",17.9),("Fred",11.5)]

# je cree une variable livreur_proche et je l'affecte  le tuple ("ben",12.4) pour initialisation

livreur_proche=livreurs_et_distance[0]

#je cree une boucle avec la variable n qui prend pour valeurs tous les tuples de livreurs_et_distance
#et je compare la distance de chaque tuple en utilisant  les indices pour atteindre les distances

for n in livreurs_et_distance: # n  dans livreurs_et_distance: designe un TUPLE
    if livreur_proche[1]>n[1]:
        livreur_proche=n
print(" Le livreur le plus proche est à",livreur_proche[1],"Km,son nom est:",livreur_proche[0])

