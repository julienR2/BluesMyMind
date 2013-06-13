import random
from phrase_chooser import *
    
def choose_phrases(key, mode, composition_length):
    #choose a list of phrases that will be used : one per 4-bar group
    
    phrase_list = []
    if composition_length == 1 :
        
        list_of_possible_1 = choose_chord_1_phrase(mode)
        
        phrase_1_index = random.randint(0, len(list_of_possible_1)-1)

        phrase_1 = list_of_possible_1[phrase_1_index]
        phrase_1_chosen = [1, phrase_1]
        #phrase_1[0]= 1
        phrase_list.append(phrase_1_chosen)
        
        list_of_possible_4 = choose_chord_4_phrase(mode)
        
        # enlever celles qui sont vraiment pas possibles a cause des differences de rythme
        
        velocity_phrase_1 = velocity_phrase(phrase_1)
        for phrase_4 in list_of_possible_4 :
            if abs(velocity_phrase(phrase_4)-velocity_phrase_1)>1 :
                list_of_possible_4.remove(phrase_4)
        
        #calcul compatibilite entre 2 phrases 1 - 4
        compatibility = []
        for phrase_4 in list_of_possible_4 :
            phrase_4_to_test = [4, phrase_4]
            compatibility.append(calcul_compatibility(phrase_1_chosen, phrase_4_to_test, key, mode))
        
        list_best_phrase_4 = get_best_options(compatibility)
        index_phrase_4 = random.randint(0, len(list_best_phrase_4)-1)
        
        phrase_4 = list_of_possible_4[index_phrase_4]
        phrase_4_chosen = [4, phrase_4]
        phrase_list.append(phrase_4_chosen)
        
        list_of_possible_5 = choose_chord_5_phrase(mode)
        velocity_phrase_4 = velocity_phrase(phrase_4)
        for phrase_5 in list_of_possible_5 :
            if abs(velocity_phrase(phrase_5)-velocity_phrase_4)>1 :
                list_of_possible_5.remove(phrase_5)
                
                
        compatibility = []
        for phrase_5 in list_of_possible_5 :
            phrase_5_to_test = [5, phrase_5]
            compatibility.append(calcul_compatibility(phrase_4_chosen, phrase_5_to_test, key, mode))
        
        list_best_phrase_5 = get_best_options(compatibility)
        index_phrase_5 = random.randint(0, len(list_best_phrase_5)-1)
        
        phrase_5 = list_of_possible_5[index_phrase_5]
        phrase_5_chosen = [5, phrase_5]
        phrase_list.append(phrase_5_chosen)
    
    
    return phrase_list




    
    
    
    
    
