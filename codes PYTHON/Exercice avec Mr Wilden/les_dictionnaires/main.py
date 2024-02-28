'''-----EXERCICE 4----'''

'''T1=[32, 5, 12, 8, 3, 75,2, 15]
T2=[]
T3=[]
for i in T1:
    if(i%2==0):
        T2.append(i)
    else:
        T3.append(i)
print(f"La liste des nombres pairs est : {T2}")
print(f"La liste des nombres impairs est : {T3}")'''



'''-----EXERCICE 5----'''

'''T1=['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
T2=[]
T3=[]
for i in T1:
    if len(i)<6:
        T2.append(i)
    else:
        T3.append(i)
print(f"La liste comportant les noms dont la taille est inferieure à 6 est {T2}")
print(f"La liste comportant les noms dont la taille est superieure à 6 est {T3}")'''

'''-----EXERCICE 8----'''
'''print("ce programme enregistre une saisie de nombres et s'arrete à la saisie d'une valeur NEGATIVE")
T1=[]
n=1
while(n>=0):
    n=float(input("Saisir une valeur,pour arreter la saise donner une valeur NEGATIVE : "))
    if n>=0 :
        T1.append(n)

petit=min(T1)
grand=max(T1)
moy=sum(T1)/len(T1)

print(f"La plus petite valeur est : {petit} ")
print(f"La plus grande valeur est : {grand} ")
print(f"La moyenne est : {moy} ")'''



'''-----EXERCICE 10----'''
'''print("Ce programme vous demande un texte et vous renvois un dictionnaire dont les cles sont les mots et les valeurs la taille de ces mots")
t=input("Saisir votre texte: ")
mot=""
T={}
c=0
for i in range(len(t)):
    while t[c]!=" ":
            mot=mot+t[c]
            c=c+1
    T[mot] = len(mot)
print("Voici le dictionnaire ainsi cree :",T)'''



'''-----EXERCICE 11----'''

'''D={ "serge"  :27, "sabine"  :11 ,"Isaac"   :17 , "Issa"   :37 ,"Armel"   :16,"jolie"   :18} for i in range(len(t)):

mineur={}
majeur={}

for i in D:          # i in D  j'accede uniquement aux Cles
    if D[i]>= 18:           # D[i] j'accede aux valeurs de ces cles
        majeur[i]=D[i]
    else:
        mineur[i]=D[i]
print(f"Le dictionnaire mineur est : {mineur}")
print(f"Le dictionnaire majeur est : {majeur}")'''


'''-----EXERCICE 12----'''

'''dicPC={"HP": 11 , "Acer": 7 , "Lenovo": 17 , "Del": 23}
dicPhone={"Sumsung": 22 , "Iphone": 9 , "Itel": 13 }
dicTablette = {"Sumland": 15 , "Other": 13}

a={** dicPC, **dicPhone, **dicTablette}
b=dict(dicPC,**dicPhone) # ne marche qu'avec deux arguments
c=dicPC|dicPhone|dicTablette
e={}
for i in [dicPC,dicPhone,dicTablette]:
    e.update(i)
print("Premiere  methode : ",a)
print("Deuxieme  methode : ",b)
print("Troisieme methode : ",c)
print("Quatrieme methode : ",e)'''

'''from turtle import *
for i in range (3) :
    forward(150)
    right(120)

for i in range (6) :
    forward(50)
    right(60)'''





