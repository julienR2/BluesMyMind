import random

def choose_progression(progression_type, nb_bars):
    if nb_bars==1:
        if progression_type == 12 :
            progression_all = (['I', 'I', 'I', 'I', 'IV', 'IV', 'I', 'I', 'V', 'IV', 'I', 'I'], ['I', 'I', 'I', 'I', 'IV', 'IV', 'I', 'I', 'V', 'V', 'I', 'I'])
            nb_progression = random.randint(0, len(progression_all)-1)
            progression = progression_all[nb_progression]

    else :
        #end = False
        if progression_type == 12 :
            progression_all = (['I', 'I', 'I', 'I', 'IV', 'IV', 'I', 'I', 'V', 'IV', 'I', 'V'], ['I', 'I', 'I', 'I', 'IV', 'IV', 'I', 'I', 'IV', 'V', 'I', 'V'], ['I', 'IV', 'I', 'I', 'IV', 'IV', 'I', 'I', 'V', 'IV', 'I', 'V'])
            nb_progression = random.randint(0, len(progression_all)-1)
            progression = progression_all[nb_progression]
    #va lancer un moteur d'inference pour choisir la progression a utiliser
    
    return progression



def on_progression_type_change(progression_type, nb_bars):
    list_progression=[]

    for n in range(0, nb_bars):
        nb_bars_left = nb_bars-n
        progression = choose_progression(progression_type, nb_bars_left)
        list_progression.append(progression)
    #on change la base de fait universelle contenant la progression du morceau
    print(str(list_progression))
    return list_progression
    