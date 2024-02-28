'''nom=""
while nom=="":
    print("donner votre nom:")
    nom=input("")
if nom!="":
    print(f' votre nom est:{nom}')'''

def demander_nom():
    nom=input("Quel est votre nom ?")
    while nom=="":
        nom = input("Quel est votre nom ?")
    if nom!="":
        return nom

def demander_age():
    age=input("Quel est votre age?")
    return int(age)

def afficher_info(a,b):
    print(f"Votre nom est {a} et vous avez {b} ans")

nom1=demander_nom()
nom2=demander_nom()
age1=demander_age()
age2=demander_age()

afficher_info(nom1,age1)
afficher_info(nom2,age2)