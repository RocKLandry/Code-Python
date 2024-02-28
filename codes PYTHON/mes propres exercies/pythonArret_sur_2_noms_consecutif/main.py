''' Ce code lit des noms de personnes et s'arrete lorsqu'on saisit deux noms consécutifs identiques et
affiche le nombre de noms saisis'''

i=0
nom1=""
nom2="*"
while nom1!=nom2:
        nom1=input(f"Donner le nom de la personne {i+1}  ")
        i=i+1
        nom2=input(f"Donner le nom de la personne {i+1}  ")
        i=i+1
print("vous avez saisi",i,"noms de personne(s)")
print("Ainsi il y a",i-1,"participants")
