'''''''------EXERCICE POUR AFFICHER UN  COEUR EN ETOILE --------'''

print("Ce programme affiche un coeur en etoile pour mon bb jolie\n")
print(" JOLIE ne Diarabi Mbi fai ")
for i in range(6):
    for j in range(7):
        if (i==0 and j%3 !=0) or (i==1 and j%3==0)or (i-j==2) or (i+j==8):
            print(" * ", end="")
        else:
            print("   ",end="")
    print()