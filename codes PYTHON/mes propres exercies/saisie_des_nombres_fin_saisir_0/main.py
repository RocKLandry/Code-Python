''' Ce code permet la saisie d'une suite de nombres jusqu'à la saisie de 0 ppour l'arret
, il renvoie le minimum de la serie puis la somme des nombres lus'''
n=int(input("Donner un nombre  "))
min=n
som=n
while n!=0:
        n=int(input("saisir une autre valeur, pour arreter la saisie donnez la valeur O  "))
        som=som+n
        if n>min:
            min=min
        else:
                min=n
print("le plus petit nombre saisi est",min,)
print("La somme des nombres est:",som)