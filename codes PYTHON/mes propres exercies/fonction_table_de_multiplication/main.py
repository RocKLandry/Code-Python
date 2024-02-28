'''Cet exercice consiste à calculer la table de multiplication d'un entier n à l'aide d'une fonction tout en précisant

la valeur de début et de fin de la multiplication'''

def table_multiplication(n):
    min=int(input("Donner la valeur de debut de la table multiplication "))
    max=int(input("Donner la valeur de fin de la  table multiplication "))
    if min>max:
        print("Erreur la valeur de debut doit etre strictement inferieur a celle de la fin")
        return
    for i in range(min,max+1):
        print(i,"X",n,"=",i*n)
        print("")

nombre=int(input("Donner la valeur de l'entier strictement positif "))
while nombre<=0:
     nombre = int(input("Donner la valeur de l'entier strictement positif "))

table_multiplication(nombre)

