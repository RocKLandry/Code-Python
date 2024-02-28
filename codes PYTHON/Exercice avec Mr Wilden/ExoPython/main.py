'''-------Exercice 14--------'''
'''print("Ce programme permet de verifier si un nombre lu est est un Carré parfais  ou pas\n")
n=int(input("Veillez saisir un nombre entier : "))
c = 0
for i in range(0,n+1,1):
    if i**2==n:
        c=1

if c==1:
    print(f"Le nombre {n} est un Carré parfait")
else:

    print(f"Le nombre {n} n'est pas un Carré parfait")'''



'''-------Exercice 15--------'''
'''print("Ce programme permet de verifier si un nombre lu est est premier ou pas1\n")
n=int(input("Veillez saisir un nombre entier : "))
c=2
for i in range(2,n):
    r=n%i
    if r==0:
        c=c+1
print("Le nombre lu a ",c,"diviseurs")
if c==2:
    print(f"{n} est un nombre premier")
else:
    print(f"{n} n'est pas un nombre premier")'''



'''-------Exercice 16--------'''
'''t=input("Veillez ecrire une chaine : ")
for i in t:
    print(i,"\n")'''


'''-------Exercice 17--------'''
'''t=input("Veillez ecrire une chaine : ")
for i in t:
    print(f"Le caractere {i} figure ",t.count(i),"fois dans la chaine t \n")'''


'''-------Exercice 18--------'''
'''print("Ce programme permet d'afficher le nombre d'occurence de la lettre 'a' et sa position dans le mot saisi")
t=input("Veillez ecrire une chaine : ")
for i in t:
    if i=='a':
        print(f"Le caractere 'a' figure  a la position",t.index(i))'''

'''-------Exercice 19--------'''
'''print("Ce programme affiche la taille de chaque element d'une liste")
l=["laptop", "iphone", "tablet"]
for i in range(len(l)):
    print(f"l'element'{l[i]}' a une taille de : {len(l[i])}\n")'''


'''-------Exercice 20--------'''
'''print("Ce programme echange le Premier et Dernier element d'une liste")
l=["laptop", "iphone", "tablet"]
print(f"Avant l'echange la liste est : {l}\n")
l[0],l[len(l)-1]=l[len(l)-1],l[0]
print(f"Apres echange la liste devient : {l}")'''

'''-------Exercice 21--------'''
'''print("Ce programme affiche le nombre de voyelles contenues dans un mot lu ")
t=input("Veillez ecrire une chaine : ")
c=0
for i in t:
    match(i):
        case "A":  c=c+1
        case "O":  c=c+1
        case "I":  c=c+1
        case "U":  c=c+1
        case "E":  c=c+1
        case "Y":  c=c+1
        case "a":  c=c+1
        case "o":  c=c+1
        case "i":  c=c+1
        case "u":  c=c+1
        case "e":  c=c+1
        case "y":  c=c+1
print(f"La chaine : {t} contient: {c} VOYELLES")'''

'''-------Exercice 21--------'''
'''print("Ce programme affiche le premier mot  d'un texte saisi ")
t=input("Veillez ecrire une chaine : ")
premierMot=""
i=0
while (t[i] != " "):
    premierMot = premierMot + t[i]
    i = i + 1
print("Le premier mot de la chaine s est  : ", t[:i])'''

'''-------Exercice 23--------'''
print("Ce programme permet de renvoyer l'extension d'un fichier saisi ")
t=input("Saisir votre fichier : ")
ext=""
j=0
for i in t:
    if i==".":
        j=t.index(".")
        while t[j]!="":
            ext=ext+t[j]
            if j<len(t):
                j=j+1

print(f"L'extension du fichier {t} est : {ext} ")




