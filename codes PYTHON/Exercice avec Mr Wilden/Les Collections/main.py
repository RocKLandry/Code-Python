

'''chaine="Aujourd'hui le cours sera tres interessant"
print(chaine)

print(chaine[0])#affiche le premier element
print(chaine[2:6])#affiche la sous chaine JOUR
print(chaine[-1])#affiche le dernier element
print(chaine[2])#affiche le 3e caractere
print(chaine[-2])# affiche l'avant dernier caractere


print("La taille de la chaine est : ",len(chaine))

print("Le nombre d'occurence de la lettre S est :",chaine.count("s"))

x="*".join(chaine)
print(x)


x="-".join(chaine)

print(x)



print(chaine.upper())

print(chaine.lower())


chaine2=chaine.replace("Aujourd'hui","Demain")
print(chaine2)

print("La taille de la chaine2 est : ",len(chaine2))

print("Le nombre d'occurence de a dans chaine2 est :",chaine2.count("a"))'''


'''l=[]
l.append(1)
l.append(3)
l.append(5)
l.append(10)
l.append(2)
l.append(4)
l.append(8)
l.append(7)
l.append(9)
l.append(6)

print(l)
print(l[3])

print("Ma liste ordonée est :",sorted(l))

print(" Le minimum de ma liste :",min(l))

print(" Le maximum de ma liste :",max(l))

print("L'index de 5 est : ",l.index(5))

L=[11,12,13,14,15]
l.extend(L)

print("La concatenation de l et L est :",l)
del l[14]
print(" Apres suppression de la valeur 15 , le tableau devient: ",l)
l.remove(1)
print(" Apres suppression de la valeur 15 et 1 , le tableau devient : ",l)'''

'''-----------EXERCICE 1----------'''
'''print("\nCe programme affiche les mois de l'annees et leurs jours dans une liste")
T1=[31,28,31,30,31,30,31,31,30,31,30,31]
T2=["Janvier","fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]
T3=[]
i=0'''

'''while i<len(T1):'''
'''for i in range(len(T1)):
    T3.append(T2[i])
    T3.append(T1[i])
    i=i+1'''

'''print(T3)'''


# APPLICATION SUR LES TUPLES

'''mon_tuple=(1,2,5,6,9,10,25,30)
mon_tuple2=(3,4,7,11,20,29)
print("Le quatrieme element du tuple est :",mon_tuple[3])


print("Le trois derniers elements du tuple sont :",mon_tuple[5:])

print("Le trois premiers elements du tuple sont :",mon_tuple[:3])

print("Le maximun du tuple est :", max(mon_tuple))

print("Le minimmun du tuple est :", min(mon_tuple))

print("La somme des elements du tuple est :", sum(mon_tuple))

print("La double concatenation du tuple est : ",mon_tuple*2)

mon_tuple3=mon_tuple+mon_tuple2

print("La concatenation de tuple1 et tuple2 est : ",mon_tuple3)'''

#EXERCIE SUR LES TUPLE

'''jour1=("Lundi","Mardi","Mercredi","Jeudi","Vendredi")
jour2=("Samedi","Dimanche")

#On teste si Samedi est un element de jour1
print("Testons si Samedi est un element de  jour1 : ","Samedi" in jour1)
#Donner la longueur de jour2
print("La longueur de jour2 est :",len(jour2))

#On teste si jour1 est egale à  jour2
print("Testons si jour1 est egale à jour2 : ",jour1 == jour2)
#Donnons le deuximeme element de jour1
print("Le deuxieme element de jour1 est : ",jour1[1])
#Donnons la partie de jour1 entre le 2e et le 4e element
print("La partie de jour1 entre le 2e et le 4e element est :",jour1[1:4])
#Indice de Dimanche dans jour2

print("L'indice de Dimanche dans jours2 est :",jour2.index("Dimanche"))

#Le nombre de Samedi dans jour1
print("Le nombre de Samedi dans jour1 est :",jour2.count("Samedi"))

#Creation d'un tuple Semaine qui est la concaatenation de jour1 et de jour2

semaine=jour1+jour2
print("Le tuple Semaine contient: ",semaine)'''


#APLICATION SUR LES DICTIONNAIRES
'''jour_sem={
    1:"Lundi",
    2:"Mardi",
    3:"Mercredi",
    4:"Jeudi",
    5:"Vendredi",
    6:"Samedi",
    7:"Dimanche"
}

print(jour_sem[7])

jour_sem[8]="Janvier"

print(jour_sem)
del jour_sem[8]

print(jour_sem)

#Parcourir les Clé de jour_sem

for i in jour_sem.keys():
    print(i)



#Parcourir les valeurs de jour_sem

for i in jour_sem.values():
    print(i)


#Parcourir la paire cle-valeurs de jour_sem

for i,j in jour_sem.items():
    print(i,j)'''



#Exercice sur Les dictionnaires

d={
    "Serge":27,
    "Sabine":11,
    "Isaac":17,
    "Issa":37,
    "Armel":16,
    "Jolie":18
  }
majeurs={  "Serge":27,"Issa":37,"Jolie":18}
mineurs={"Sabine":11, "Isaac":17,"Armel":16}







