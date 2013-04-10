def choose_progression(progression_type, nb_bars):
    if nb_bars==1:
        #end = True
        progression = ['I', 'I', 'I', 'I', 'IV', 'IV', 'I', 'I', 'V', 'IV', 'I', 'I']
    else :
        #end = False
        progression = ['I', 'I', 'I', 'I', 'IV', 'IV', 'I', 'I', 'V', 'IV', 'I', 'V']
    
    #va lancer un moteur d'inference pour choisir la progression a utiliser
    
    return progression
