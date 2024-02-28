'''print("Exercice 1")
print("Ce programme affiche les 10 entiers suivants un nombre lu")
n=int(input("\nDonner l'entier de depart : "))
print("\n")
max=n+10
for i in range(n+1,max+1):
    print(i,end=" ")'''

'''print("Exercice 2")
print("Ce programme affiche tous les diviseurs d'un nombre entier non nul")
n=int(input("\nDonner l'entier non nul : "))
if(n<=0):
    while(n<=0):
        n = int(input("\nDonner l'entier non nul : "))

print(" les diviseurs de", n, "sont : \n")
for i in range(n,0,-1):
        if(n%i==0):
         print(i,end=" ")'''


'''print("EXERCICE 3")
print("Ce programme detemine l'annee au cours de laquelle la population de Kolda depassera celle de Dakar")
popuDak=7000000
popuKol=500000
n=2023
while(popuKol<=popuDak):
    popuDak=popuDak+50000
    popuKol=popuKol+popuDak*0.08
    n=n+1
print(f"La population de Kolda depassera celle de Dakar en : {n} \npopulation de Dakar : {popuDak}\npopulation de Kolda : {popuKol}")'''




'''print("EXERCICE 4")
print(" Ce programme calcule le terme Un  d'une suite U en fonction d'un rang n donné")
n=int(input("\n Donner le rang du terme   : "))
Un=6
i=1

while(i<=n+1):
        Sn=4*Un+10
        Un=Sn
        i=i+1
print(f" Au rang n={n} la suite a  pour valeur : { Sn }")'''







'''print("EXERCICE 5")
print(" Ce programme calcule le terme Un  d'une suite de Fibonacci U en fonction d'un rang n > 2 donné")
n=int(input("\n Donner le rang du terme  > 2 : "))
if(n<=2):
    while(n<=2):
        n = int(input("\n Donner le rang du terme  > 2 : "))
else:
    Un=0
    Up=1
    i=1
    while (i <=n+1): #j'ai mis n+1 par ce que de 0 à n il y'a eu (n+1) ittération
        Sn=Up+Un
        Un=Up
        Up=Sn
        i = i + 1
print(f" Au rang = {n} la suite a  pour valeur : {Sn}")'''



'''print("EXERCICE 6")
print("Ce programme vous demande de deviner un nombre entier choisi aleatoirement par l'ordinateur")
import random
n=random.randint(1,30)
print("\nVeillez saisir un nombre entier ! Vous avez 5 tentatives\n")
for i in range(5):
    choix=int(input("Votre choix : "))
    if(choix==n):
        print("\nBonne reponse")
    elif(choix>n):
        print("Ce nombre est trop Grand")
    else:
        print("Ce nombre est trop Petit")'''

'''print("EXERCICE 7")
print("Ce programme affiche le nombre de chiffre(s) composant un nombre lu")
n=int(input("Veillez saisir un nombre : "))
print("le nombre:",n,"est compose de",len(str(n)),"chiffres")'''



'''print("EXERCICE 10")
print("Ce programme verifie si un nombre entier lu est parfait ou pas ")
n=int(input("Veillez saisir la valeur d'un entier non nul : "))
if(n==0):
    while(n==0):
        n = int(input("Veillez saisir la valeur d'un entier non nul : "))
else:
    som=0
    for i in range(n, 0, -1):
        if (n % i == 0):
            if(i!=n):
                som=som+i
    if(n==som):
        print(f"{n} est un nombre PARFAIT")
    else:
        print(f"{n} n'est pas un nombre PARFAIT")'''


'''print(" EXERCICE 18")
print(" Ce programme affiche les equivalents de l'euro € du dollar $ \n")
for i in range(1,16384+1):
    print(f" {i} euro(s)€ = {i*1.65} dollar $\n")'''


'''print(" EXERCICE 19")
print(" Ce programme affiche les 20 premiers termes de la de multiplication par 7\n puis ajoute le symbole * apres chaque multiple de 3\n")
for i in range (1,20+1):
    print(i*7,end="  ")
    if(i%3==0):
        print( i * 7,"*", end="  ")'''

'''print(" EXERCICE 15")
print("Ce programme affiche un coeur avec le symbole *\n")

for i in range(6):
    for j in range(7):
        if(((i==0)and(j==1))or((i==0)and(j==2))or((i==0)and(j==4))or((i==0)and(j==5))or((i==1)and(j==0))or((i==1)and(j==3))or((i==1)and(j==6))or((i==2)and(j==0))or((i==2)and(j==6))or((i==3)and(j==1))or((i==3)and(j==5))or((i==4)and(j==2))or((i==4)and(j==4))or((i==5)and(j==3))):
            print("*",end=" ")
        else:
            print(" ")'''






