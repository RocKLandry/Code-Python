"""Dans cet exercice nous allons cerrer une liste de jours de la semaines puis acceder de deux manieres
differentes aux 5 premiers jours  puis aux 2 derniers jours """

la_semaines=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
jours_ordinaires=la_semaines[0:5]
week_end=la_semaines[5:7]
print(jours_ordinaires)
print(week_end)
jour_ordi1=[]
week_end1=[]
for i in range(5):
    jour_ordi1.append(la_semaines[i])
for i in range(2):
    week_end1.append(week_end[i])
print(jour_ordi1)
print(week_end1)

# Accedons à present de deux manieres differentes au dernier jour de la liste

dernier_jour1=la_semaines[-1]
#dernier_jour2=

print(dernier_jour1)
la_semaines_inverse=la_semaines
