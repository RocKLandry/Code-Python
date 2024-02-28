'''Ce code permet d'afficher 4 nombres lus au clavier dans l'ordre croissant'''

a=int(input("Saisir le premier nombre  "))
b=int(input("Saisir le deuxieme nombre  "))
c=int(input("Saisir le troisieme nombre  "))
d=int(input("Saisir le quatrieme nombre  "))

'''Declaration des variables des differentes positions des variables a,b,c et d'''
premier=0
deuxieme=0
troisieme=0
quatrieme=0
premier=a
if b<premier:
    deuxieme=premier
    premier=b
else:
    deuxieme=b
if c<premier:
    troisieme=deuxieme
    deuxieme=premier
    premier=c
elif c<deuxieme:
    troisieme=deuxieme
    deuxieme=c
else:
    troisieme = c
if d<premier:
    quatrieme=troisieme
    troisieme=deuxieme
    deuxieme=premier
    premier=d
elif d<deuxieme:
    quatrieme=troisieme
    troisieme=deuxieme
    deuxieme=d
elif d<troisieme:
    quatrieme=troisieme
    troisieme=d
else:
    quatrieme=d

print("voici les nombres saisis dans l'ordre croissant:")
print(premier)
print(deuxieme)
print(troisieme)
print(quatrieme)

