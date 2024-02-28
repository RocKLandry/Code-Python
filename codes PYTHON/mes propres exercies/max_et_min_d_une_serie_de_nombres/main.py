'''Ce code permet le saisie de plusieurs nombres et s'arrete si l'on rentre la valeur 0
ensuite il renvoie le min ,le max puis la somme de tous les nombres saisis'''
n=int(input("Donner le premier nombre de la liste  "))
min=n
max=n
som=n
if n<0:
    print("Vous avez saisi un nombre negatif! La liste s'arrete!")
    print("La somme des nombres saisis est: 0")
    print("Le minimun de la liste est: 0")
    print("Le maximun de la liste est: 0")
else:
    while n >= 0:
        n = int(input("Donner les nombres suivants, saisir un nombre negatif pour arreter la saisie  "))
        if n >= 0:
            som = som + n
            if min > n:
                min = n
            elif max < n:
                max = n

    print("La somme des nombres saisis est", som)
    print("Le minimun de la liste est:", min)
    print("Le maximun de la liste est:", max)



