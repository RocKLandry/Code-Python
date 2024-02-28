'''-----DEVOIR DE LANDRY MOUSSOYI-------'''

'''-----PROJET 1-----'''
"""

LivreBD={ 
          "Les misérables":("Victor Hugo",5),
          "Le dernier des Mohicans":("James F. Cooper",0),
          "Un animal doué de raison":("Robert Merle",6),
          "Le grand Meaulnes":("Alain Fournier",1),
          "Notre Dame de Paris":("Victor Hugo",4),
          "Les comtemplations":("Victor Hugo",0),
         }

'''----Question 1----'''
def auteurs(t):
    liste=[]
    for i in t:
        liste.append(t[i][0])
    return liste


liste_retournee=auteurs(LivreBD)
print("Les auteurs des livres sont : ",liste_retournee)

'''----Question 2----'''

def titres_empruntables(t):
    liste =[]
    for i in t:
        if t[i][1]>0:
            liste.append(i)
    return liste
livres_empruntables=titres_empruntables(LivreBD)

print("Les livres empruntables sont : ",livres_empruntables)

'''----Question 3----'''

def titres_auteurs(nom,t):
    liste=[]
    for i in t:
       if t[i][0]==nom:
           liste.append(i)
    return liste

nom_auteur=input("Veillez saisir le nom d'un Auteur :  ")
roman_auteur=titres_auteurs(nom_auteur,LivreBD)

print(f"Les Livres Ecrits par l'auteur : {nom_auteur} sont : {roman_auteur}")"""



'''-----PROJET 2-----'''

"""
def argent_au_total():
    somme=float(input("Quelle est la somme totale que vous voulez placer : "))
    while somme<0:
        print("Erreur ! Veillez saisir que des valeurs positives")
        somme = float(input("Quelle est la somme totale que vous voulez placer : "))
    
    
    n=int(input("Donner le nombre d'année pour lequel vous voulez placer votre argent : "))
    while n<0:
        print("Erreur ! Veillez saisir que des valeurs positives")
        n = int(input("Donner le nombre d'année pour lequel vous voulez placer votre argent : "))
    
    taux=float(input("Quel est votre taux d'interet : "))
    while taux < 0:
        print("Erreur ! Veillez saisir que des valeurs positives")
        taux = float(input("Quel est votre taux d'interet : "))/100

    RetCapIvs=somme+(1+taux)*n
    print("Votre retour sur le capital investit est : ",RetCapIvs)

argent_au_total()"""

'''-----PROJET 3-----'''



poule = int(input("Donner le nombre de poules tuées : "))
chien = int(input("Donner le nombre de Chiens tués : "))
vache = int(input("Donner le nombre de vaches tués : "))
ami = int(input("Donner le nombre d'ami tués : "))

def amende(Poule,Chien,Vache,Ami):
    capital=0
    if Poule>=1:
        for i in range(Poule):
            capital=capital+1
    if Chien>=1:
        for i in range(Chien):
            capital=capital+3
    if Vache>=1:
        for i in range(Vache):
            capital=capital+5
    if Ami>=1:
        for i in range(Ami):
            capital=capital+10
    return capital
debourse=amende(poule,chien,vache,ami)
print("Le montant du par le chasseur est : ",debourse)
print("\nLa somme que le chasseur doit débourser est : ",debourse +100)