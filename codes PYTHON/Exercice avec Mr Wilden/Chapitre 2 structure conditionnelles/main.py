'''print("Exercice 1")
print(" Ce programme verifie si deux nombres lus ont le meme signe ")
a=float(input(" Donner le premeier nombre : "))
b=float(input(" Donner le deuxieme nombre : "))
if((a<0)and(b<0))or((a>0)and(b>0)):
    print(" Les deux nombres ont le meme signe")
else:
    print(" Les deux nombres n'ont pas le meme signe")'''


'''print(" EXERCICE 2")
a=float(input(" Donner le premeier nombre : "))
b=float(input(" Donner le deuxieme nombre : "))
if (a*b>0):
    a,b=b,a
else:
    a,b=a+b,a*b
print(f"La valeur de a est : {a} et celle de b est {b}"  )'''


'''print(" EXERCICE 3")
print("\n Ce programme donne la categorie d'une personne en fonction de son age")
age=0
while(age<6):
    age = int(input(" \nVeiller saisir un age correcte : "))
if((age>=6)and(age<=7)):
    print(" Vous etes POUSSIN")
elif((age>=8)and(age<=9)):
    print(" Vous etes PUPILLE")
elif((age>=10)and(age<=11)):
    print(" Vous etes MINIME")
else: print(" Vous etes CADET")'''


'''print(" EXERCICE 4")
print(" Ce programme calcule la moyenne d'un etudiant avec 3 notes")
note=-1
somme =0
for i in range(3):
    note = float(input(" Saisir une note correcte :  "))
    if ((note >= 0) and (note <= 20)):
        somme = somme + note
    else:
        while((note<0)or(note>20)):
            note = float(input(" Saisir une note correcte :  "))



moy=somme/3
if(moy>=16):
    print(f" Votre moyenne est : {moy}  avec la mention : TRES BIEN")
elif((moy>=14)and(moy<=16)):
    print(f" Votre moyenne est : {moy}  avec la mention : BIEN")
elif((moy>=12)and(moy<=14)):
    print(f" Votre moyenne est : {moy}  avec la mention : ASSEZ BIEN")
elif ((moy >= 10) and (moy <= 12)):
    print(f" Votre moyenne est : {moy}  avec la mention : PASSABLE")
else: print(f" Votre moyenne est : {moy}  avec la mention : INSUFFISANT")'''





'''print("  Exercice 5 ")
print("  Ce programme determine le Prix_TTC d'un produit connaissant son Prix_HT et sa categorie ")
prixHT=0

while(prixHT<=0):
    prixHT=float(input("  Veillez saisir le prix correcte du produit : "))

print("  Donnez la categorie du produit \n  A\n  B\n  C")
cat=input("  Categorie : ")
if((cat=="A")or(cat=="a")):

     prixTTC=prixHT+prixHT*0.07
     print(f" Le PrixTTC du produit est {prixTTC} FCFA")

elif((cat=="B")or(cat=="b")):

    prixTTC = prixHT + prixHT * 0.2
    print(f" Le PrixTTC du produit est {prixTTC} FCFA")

elif((cat=="C")or(cat=="c")):

    prixTTC = prixHT + prixHT * 0.25
    print(f" Le PrixTTC du produit est {prixTTC} FCFA")

else:  print(f"\n  Mauvaise saisie de la categorie")'''


'''print(" Exercice 6 ")
print(" Ce programme verifie si un nombre est divible par 3 et 13 ou non")
n=int(input(" Veillez saisir un nombre entier : "))
if((n%3==0)and(n%13==0)):
    print(f" {n} est divisible par 3 et 13 ")
else: print(f" {n} n'est pas divisible par 3 et 13")'''




'''print(" Exercice 7 ")
print("Ce programme determine le maximum et le minimum de trois nombres lus")
for i in range(3):
    n=int(input("Donner un nombre : "))
    if(i==0):
        max=n
        min=n
    else:
        if(n>max):
            max=n
        elif(n<min):
            min=n

print("\n Le maximum est : ",max)
print("\n Le minimum est : ", min)'''


'''print(" Exercice 8 ")
print("Ce programme verifie si un nombre est pair ou pas")
n=int(input("Donner un nombre entier  : "))
if(n%2==0):print(f"{n} est pair")
else:print(f"{n} est impair")'''


'''print(" Exercice 9 ")
print(" Ce programme verifie si une lettre est une voyelle ou une consonne")
c=input(" Veillez saisir une lettre : ")
match(c):
    case "A": print(" A est une voyelle")
    case "O": print(" U est une voyelle")
    case "I": print(" I est une voyelle")
    case "U": print(" U est une voyelle")
    case "E": print(" E est une voyelle")
    case "Y": print(" Y est une voyelle")
    case "a": print(" a est une voyelle")
    case "o": print(" o est une voyelle")
    case "i": print(" i est une voyelle")
    case "u": print(" u est une voyelle")
    case "e": print(" e est une voyelle")
    case "y": print(" y est une voyelle")
    case _: print(" Le caractere saisi est une consonne")'''





'''print(" Exercice 10 A ")
print("Ce programme vous indique le nom d'un jour de la semaine en fonction de son numero")
n=int(input("\nDonner le numero du jour de 1 à 7 : "))
match(n):
    case 1: print(" LUNDI ")
    case 2: print(" MARDI")
    case 3: print(" MERCREDI ")
    case 4: print(" JEUDI")
    case 5: print(" VENDREDI ")
    case 6: print(" SAMEDI")
    case 7: print(" DIMANCHE ")
    case _: print(" Le numero ne correspond à aucun Jour")'''


'''print(" Exercice 10 B ")
print("\n Ce programme vous indique le nombre de jours d'un mois de l'annee en fonction de son numero")
a=int(input("Saisir le numero du mois de 1 à 12 : "))
match(n):
    case 1: print(" JANVIER 31 jours")
    case 2: print(" FEVRIER 28 jours")
    case 3: print(" MARS 31 jours")
    case 4: print(" AVRIL 30 jours")
    case 5: print(" MAI 31 jours")
    case 6: print(" JUIN 30 jours")
    case 7: print(" JUILLET 31 jours")
    case 8: print(" AOUT 31 jours")
    case 9: print(" SEPTEMBRE 30 jours")
    case 10:print(" OCTOBRE 31 jours")
    case 11:print(" NOVEMBRE 30 jours")
    case 12:print(" DECEMBRE 31 jours")
    case _: print(" Le numero ne correspond à aucun mois")'''


'''print(" Exercice 10 C ")
print(" Ce programme verifie si une année est bisextille ou pas ")
annee=int(input(" Saisir l'année : "))
if((annee%4==0)and(annee%100!=0)):
    print(f" L'annee: {annee} est bisextille ")
elif((annee%4==0)and(annee%100==0)and(annee%400==0)):
    print(f" L'annee: {annee} est bisextille ")
else:  print(f" L'annee : {annee} n'est pas bisextille ")'''







'''print(" Exercice 11 ")
print(" Ce programme effectue une operation selon votre choix")
a = float(input(" Donner le premeier nombre : "))
b = float(input(" Donner le deuxieme nombre : "))
choix = input(
    " Taper 1) pour  ADDITION \n Taper 2) pour SOUSTRACTION \n Taper 3) pour MULTIPLICATION\n Taper 4) pour DIVISION \n Taper 5) pour DIVISION ENTIERE \n Taper 6) pour RESTE DE LA DIVIDION ENTIERE  \n Entrer Votre choix : ")
match choix:
    case "1":
        print(f" La somme de {a} et {b} est {a + b}")

    case "2":
        print(f" La difference de {a} et {b} est {a - b}")

    case "3":
        print(f" La multiplication de  de {a} et {b} est {a * b}")

    case "4":
        if (b == 0):
            print("La division par 0 est impossible")
        else:
            print(f" La division de  de {a} par {b} est {a / b}")

    case "5":
        if b != 0:
            print(f" La division entiere de {a}  par {b} est {a // b}")
        else:
            print("La division par 0 est impossible")

    case "6":
            if (b == 0):
                    print("La division par 0 est impossible")
            else:
                    print(f" Le reste de la division de {a} par {b} est {a % b}")
    case _:
            print(" Mauvaise manipulation")'''







'''print("Exercice 12")
print("Ce programme affiche si une personne est imposable")
print("Saisir le sexe de la persone \nM pour Homme  \nF pour Femme")
sexe=input(" votre choix : ")
age=int(input("Donner l'age de la personne : "))
if((sexe=='M')and(age>=21)):
    print(" Cet Homme est imposable")
elif((sexe=='F')and(age>=18)and(age<=25)):
    print('Cette Femme est imposable')
else:
    print("Cette personne ne paie pas l'impot")'''


'''print("Exercice 13")
print("Ce programme est un Quizz")
n=int(input("Question 1: Combien de fois lafrance a t'elle remporté la coupe du monde ? : "))
if(n!=2):print("Mauvaise réponse ! essayez une autre Question")
else: print("Bonne réponse")
print("\nQuelle est la capitale du Japon ?\nA:Damas\nB:Bamako\nC:Tokyo")
j=input("Votre choix : ").upper()   #cette methode transforme un mot ou lettre en Majiscule
if(j=="C"): print("Bonne réponse")
else:print("Mauvaise réponse ! essayez une autre Question")
print("En quelle année a pris fin la seconde guerre mondiale ?\nA:1945\nB:1939\nC:1918")
p=input("Votre choix : ").lower()   #cette methode transforme un mot ou lettre en Miniscule
if(p=="a"): print("Bonne réponse")
else:print("Mauvaise réponse ! désolé")'''


'''print("Exercice 14")
print("Ce programme permet de deplacer une personne en fonction d'un nombre entier lu ")
print("\nSaisir un entier \n2: La personne part en Haut\n4: La personne part à Gauche\n6: La personne part à Droite\n8: La personne part en Bas ")
choix=int(input("\nVotre choix : "))
match choix:
    case 2: print(" La personne part en Haut")
    case 4: print("La personne à Gauche")
    case 6: print("La personne part à Droite")
    case 8: print("La personne par en Bas")
    case _: print("Saisie incorrecte ! la personne ne bouge pas !")'''


'''print("Exercice 15")
print("Ce programme verifie si un nombre appartient à un intervalle ou pas")
inf=float(input("Donner la borne inferieure : "))
sup=inf
while(sup<=inf):
    sup=float(input("\nDonner la borne superieure correcte: "))
n=float(input("\nDonner la Valeur du nombre : "))
if((n>=inf)and(n<=sup)):print(f"{n} appartient à l'intervalle")
else:print(f"{n} n'appartient pas à l'intervalle")'''


'''print("Exercice 16")
print("Ce programme permet de calculer le montant des heures supplementaires")
heure=int(input(" Donner le nombre d'heurre effectuées : "))
while(heure<=0):heure=int(input(" Donner le nombre d'heurre effectuées correcte : "))
sal=float(input("\nDonner le prix unitair d'une heure : "))
while(sal<=0):sal=float(input("\nDonner le prix unitair d'une heure correcte : "))
if(heure<39):print(f"\n votre montant des heures supplementaires est de : {sal*39}")

elif((heure>=40)and(heure<=44)):
    montant=sal+sal*0.5
    print(f"\n votre montant des heures supplementaires est de : {montant}")

elif((heure>=45)and(heure<=49)):
    montant = sal + sal * 0.75
    print(f"\n votre montant des heures supplementaires est de : {montant}")

elif(heure>=50):
    montant = sal + sal
    print(f"\n votre montant des heures supplementaires est de : {montant}")'''





'''for i in range(2,500,2):
    print(i,end=" ")'''
