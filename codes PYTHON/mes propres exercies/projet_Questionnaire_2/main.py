'''Dans cet exercice nous allons reproduire le projet questionnaire mais en utilisant les tuples et
listes'''

'''
#Dansun premiertemps je cree des tuples des tuples qui sont mes variables à fournir en paramettre

question1=('Quelle est la capitale de la chine ?',('paris','pekin','dolisie'),"pekin")
question2=("Quelle est la capitale de la cote d'ivoire ",('abidjan','kinshasa','bamako'),"abidjan")
question3=('Quelle est la capitale du congo ?',('lome','yaounde ','brazzaville'),"brazzaville")

score=0

def poser_question(titre_question):
    global score
    rep =titre_question[1]
    a = rep[0]
    b = rep[1]
    c = rep[2]
    print("Question :")
    print(titre_question[0])
    print(" ",a)
    print(" ",b)
    print(" ",c)

    choix=input('Votre reponse :  ')
    if choix.lower()==titre_question[2].lower():
# choix.lower() converti la reponse du choix en miniscuele  et choix.epper() en majiscule
        print("Bonne reponse")
        score=score+1

    else:
        print("Mauvaise reponse")


poser_question(question1)
print("")
poser_question(question2)
print("")
poser_question(question3)
print("")
print("Score total:",score)

'''

''' On refait le meme code mais avec une  boucle cette fois pour afficher les differentes reponses possibles'''


def demander_nombre(max):
    n_str = input("Donner un entier compris entre 1 et " + str(max) + "  ")
    try:
        n_int = int(n_str)
        if 1 <= n_int <= max:
            return n_int
        print("Erreur vous devriez saisir un nombre entre 1 et", max)
    except:
        print("Erreur  veillez saisir que des chiffres")

        '''
        En cas d'erreur  c'est a dire ( soit la saisie d'un caratere ou d'un nombre  qui n'est pas sur la liste
        des reonses ), on utlise recurssivement la fonction demander_nombre  
        '''
    return demander_nombre(max)


def poser_question(titre_question):
    etat_reponse = False
    rep = titre_question[1]
    print("Question :")
    print(titre_question[0])
    for i in range(len(rep)):
        print(f"{i + 1}-", rep[i])

    choix = demander_nombre(len(rep))
    if rep[choix - 1].lower() == titre_question[2].lower():
        # choix.lower() converti la reponse du choix en miniscuele  et choix.epper() en majiscule
        print("Bonne reponse")
        etat_reponse = True

    else:
        print("Mauvaise reponse")
    return etat_reponse


questionnaire = {
    ('Quelle est la capitale de la chine ?', ('paris', 'pekin', 'dolisie'), "pekin"),
    ("Quelle est la capitale de la cote d'ivoire ", ('abidjan', 'kinshasa', 'bamako'), "abidjan"),
    ('Quelle est la capitale du congo ?', ('lome', 'yaounde ', 'brazzaville'), "brazzaville")
}


def lancer_questionnaire(questionnaire):
    score = 0
    for i in questionnaire:
        if poser_question(i):  # on teste si poser_question est True
            score += 1
        print("")
    print("Score total:", score, "sur", len(questionnaire))


lancer_questionnaire(questionnaire)



