from phrases import PHRASE_MIDDLE
import mingus.core.intervals as intervals
import random
import mingus.core.notes as notes
    
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
            compatibility.append(calcul_compatibility(phrase_1, phrase_4, key))
        
        list_best_phrase_4 = get_best_options(compatibility)
        index_phrase_4 = random.randint(0, len(list_best_phrase_4)-1)
        
        phrase_4 = list_of_possible_4[index_phrase_4]
        phrase_4_chosen = [4, phrase_4]
        #phrase_4[0] = 4
        phrase_list.append(phrase_4_chosen)

        list_of_possible_5 = choose_chord_5_phrase(mode)
        velocity_phrase_4 = velocity_phrase(phrase_4)
        for phrase_5 in list_of_possible_4 :
            if abs(velocity_phrase(phrase_5)-velocity_phrase_4)>1 :
                list_of_possible_5.remove(phrase_5)
                
                
        compatibility = []
        for phrase_5 in list_of_possible_5 :
            compatibility.append(calcul_compatibility(phrase_4, phrase_5, key))
        
        list_best_phrase_5 = get_best_options(compatibility)
        index_phrase_5 = random.randint(0, len(list_best_phrase_5)-1)
        
        phrase_5 = list_of_possible_5[index_phrase_5]
        phrase_5_chosen = [5, phrase_5]
        #phrase_5[0] = 5
        phrase_list.append(phrase_5_chosen)
        
        
    
    elif composition_length == 2 :
        nb_phrases = 5
    
    
    return phrase_list

def choose_chord_1_phrase(mode):
    list = []
    for phrase in PHRASE_MIDDLE :
        if 1 in phrase[0] and phrase[2]==mode:
            list.append(phrase)          
    return list    

def choose_chord_4_phrase(mode):
    list = []
    for phrase in PHRASE_MIDDLE :
        if 4 in phrase[0] and phrase[2]==mode:
            list.append(phrase)          
    return list

def choose_chord_5_phrase(mode):
    list = []
    for phrase in PHRASE_MIDDLE :
        if 5 in phrase[0] and phrase[2]==mode:
            list.append(phrase)          
    return list



def calcul_compatibility(phrase1, phrase2, key):
    compatibility = 0
    percent = common_note(phrase1, phrase2, key)
    
    if percent > 9 and percent < 20 :
        compatibility += 2
    
    elif percent > 19 and percent < 30 :
        compatibility += 4
    
    elif percent > 29 and percent < 40 :
        compatibility += 6
    
    elif percent > 39 and percent < 50 :
        compatibility += 4
    
    elif percent > 49 and percent < 60 :
        compatibility += 2
    
    gap = gap_last_first_note(phrase1, phrase2, key)
    
    if gap < 15 :
        compatibility += 14 - gap
    
    return compatibility
    
    
def get_best_options(list):
    result = []
    best_compatibility = max(list)
    for i,j in enumerate(list):
        if j==best_compatibility:
            result.append(i)
            
    return result

def gap_last_first_note(phrase1, phrase2, key):    
    last_note_1 = phrase1[3][phrase2[1]-1][-1:][0]
    last_note_2 = phrase2[3][phrase2[1]-1][-1:][0]
    last_note_1 = get_note(last_note_1, key)
    last_note_2 = get_note(last_note_2, key)
    return intervals.measure(last_note_1, last_note_2)

def common_note(phrase1, phrase2, key):
    phrase1_list = []
    percentage = 0
    number_notes = 0
    for bars in  phrase1[3] :
        for n in bars :
            notes = get_note(n, key)
            phrase1_list.append(notes)
    for bars in phrase2[3] :
        for n2 in bars :
            number_notes+=1
            if get_note(n2, key) in phrase1_list:
                percentage+=1
    
    return (percentage/number_notes)*100


def velocity_phrase(phrase):
    print(str(phrase))
    number_notes = 0
    for bars in phrase[3] :
        for note in bars :
            number_notes+=1
    
    if number_notes < 4*phrase[2] :
        return 1 #plutot lent
    
    elif number_notes < 7*phrase[2]  :
        return 2 #plutot moyen
    
    else :
        return 3 #plutot rapide
    

def get_note(n, key):
    note = intervals.unison(key)
    if n[0] == 1 :
        note = intervals.unison(key)
    elif n[0] == 2 :
        note = intervals.second(key, key)
    elif n[0] == 3 :
        note = intervals.third(key, key)
    elif n[0] == 4 :
        note = intervals.fourth(key, key)
    elif n[0] == 5 :
        note = intervals.fifth(key, key)
    elif n[0] == 6 :
        note = intervals.sixth(key, key)
    elif n[0] == 7 :
        note = intervals.seventh(key, key)

    if n[3] == "bemol":
        note = notes.diminish(note)
    elif n[3] == "diese" :
        note = notes.augment(note)
    return note
    
    
    
    
    
