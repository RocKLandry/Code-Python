'''def table_de_8():
    for i in range(11):
        #print(f"{8} X {i} = {8*i}",end=" ")
        print(8*i,end=" ")

table_de_8()
'''
'''def table_de_n(n):
    for i in range(11):
        a=n*i
        print(a, end=" ")
       #print(n* i, end=" ")

print(table_de_n(5))'''



'''def table_de_8(n):
    i=0
    while i<=10:
        print(n*i,end=" ")
        i=i+1
a=int(input("Veillez saisir la valeur du multiplicateur : "))
table_de_8(a)'''




''''-----EXERCICE 12 avec des fonctions-------'''

'''dicPC = {"HP": 11, "Acer": 7, "Lenovo": 17, "Del": 23}
dicPhone = {"Sumsung": 22, "Iphone": 9, "Other": 13}
dicTablette = {"Sumsung": 15, "Other": 13}
def concatenation(a,b,c):
    t={}
    for i in [a,b,c]:
        t.update(i)
    return t

print(concatenation(dicPC,dicPhone,dicTablette))'''



'''-----EXERCICE ADMIS ECHOUES----'''

'''moyenne={
"Etudiant 1": 6,
"Etudiant 2": 10,
"Etudiant 3": 11,
"Etudiant 4": 14,
"Etudiant 5": 8,
"Etudiant 6": 9,
"Etudiant 7": 10,
"Etudiant 8": 7
        }
def afficher(t):
    s=0
    adm={}
    ech={}
    for i in t:
        s=s+t[i]
    m=s/len(t)
    print("\t")
    print("La moyenne des etudiants est : ",m)
    for j in t:
        if (t[j]>=m):
            adm[j]=t[j]
        else:
            ech[j] = t[j]
    return adm,ech


a,b=afficher(moyenne)
print("La liste des etudiants est   : ",moyenne)
print("La liste des admis est       : ",a)
print("La liste des echoues est     : ",b)'''


'''------EXERCICE KB------'''


def devenir_analyste(b):
    competence_a_avoir=["python","excel","sql","machine learning","statistique","cloud computing","spark","hadoop","deep learnig"]
    competence_en_commun=[]
    for i in b:
        for j in competence_a_avoir:
            if i==j:
                competence_en_commun.append(i)

    print(f"Vous aviez deja : {competence_en_commun} comme competences necessaire pour devenir Analyste, Continuez comme ça!")


competence_que_j_ai=[]
competence=' '
while(competence!=''):
    competence=input("Veillez saisir une competence  ! pour arreter la saisie n'ecrivez rien : ")
    competence_que_j_ai.append(competence)


devenir_analyste(competence_que_j_ai)


'''import math
print(dir(math))'''

'''import pyttsx3
engine = pyttsx3.init()
engine.say("nakamou ?")
engine.runAndWait()'''



