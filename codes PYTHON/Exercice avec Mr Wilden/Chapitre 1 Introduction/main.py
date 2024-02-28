'''print("*******EXERCICE 1******")
nom=input("Donner le nom de l'etudiant: ")
age=int(input("donner l'age de l'etudiant: "))
print("Bonjour",nom,"tu as ",age," ans","Bienvenue à ICAGI")'''

'''print("*******EXERCICE 2 ******")

anneeNss=int(input("Saisir l'année de naissance : "))
anneeActu=int(input("Saisir l'année actuelle : "))
age=anneeActu-anneeNss
print(" Vous avez :",age," ans")'''

'''a=float(input("Donner le premier nombre : "))
b=float(input("Donner le deuxieme nombre: "))
if (a>b):
    print(a," est superieur à ",b)
elif(a==b):
    print(b, " est egale à ", a)
else:
    print(b, " est inferieur à ", a)


x=float(input("Donner un entier"))
if(x%2==0):
    print(x,"est pair")
else:
    print(x, "est impair")'''


''' print("*******EXERCICE 3******")'''
'''L=int(input(" Donner la longueur du rectangle : "))
l=int(input(" Donner la largeur du rectangle : "))
p=(L+l)*2
s=L*l
print(f" Le perimetre est : {p}")
print(f" La surface est : {s}")
print(" Merci d'avoir executer le code")'''


''' print("*******EXERCICE 4******")'''
'''print(" Ce programme calcule la puissance d'un entier X ")
x=int(input(" Donner la valeur de X : "))
y=-1
while(y<0):
    y = int(input(" Donner la valeur de l'exposant strictement positif: "))
print(f" {x} à la puissance {y} est : {x**y}")'''

print("*******EXERCICE 5******")
print(" Ce programme permute la valeur de deux entiers A et B")
a=int(input(" Donner la valeur de A : " ))
b=int(input(" Donner la valeur de B : " ))
a,b=b,a

print(f" La nouvelle valeur de A est: {a}" )
print(f" La nouvelle valeur de B est: {b}" )
