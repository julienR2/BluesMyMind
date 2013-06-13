from note_utils import get_note
from phrases import PHRASE_MIDDLE
import mingus.core.intervals as intervals


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



def calcul_compatibility(phrase1, phrase2, key, mode):
    compatibility = 0
    percent = common_note(phrase1, phrase2, key, mode)
    
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
    
    gap = gap_last_first_note(phrase1, phrase2, key, mode)
    
    if gap < 12 :
        compatibility += 11 - gap
    
    return compatibility
    
    
def get_best_options(list):
    result = []
    best_compatibility = max(list)
    for i,j in enumerate(list):
        if j==best_compatibility:
            result.append(i)
            
    return result

def gap_last_first_note(phrase1, phrase2, key, mode): 
    
    key1 = key
    key2 = key
    if mode != "none" : 
        if phrase1[0]==0 :
            key1 = key
        elif phrase1[0]==4 :
            key1 = intervals.fourth(key, key)
        elif phrase1[0]==5:
            key1 = intervals.fifth(key, key)
            
        if phrase2[0]==0 :
            key2 = key
        elif phrase2[0]==4 :
            key2 = intervals.fourth(key, key)
        elif phrase2[0]==5:
            key2 = intervals.fifth(key, key)
          
    last_note_1 = phrase1[1][3][phrase2[1][1]-1][-1:][0]
    last_note_2 = phrase2[1][3][phrase2[1][1]-1][-1:][0]
    last_note_1 = get_note(last_note_1, key1)
    last_note_2 = get_note(last_note_2, key2)
    return intervals.measure(last_note_1, last_note_2)

def common_note(phrase1, phrase2, key, mode):
    phrase1_list = []
    percentage = 0
    number_notes = 0
    key1 = key
    key2 = key
    
    if mode != "none" :     
        if phrase1[0]==0 :
            key1 = key
        elif phrase1[0]==4 :
            key1 = intervals.fourth(key, key)
        elif phrase1[0]==5:
            key1 = intervals.fifth(key, key)
            
        if phrase2[0]==0 :
            key2 = key
        elif phrase2[0]==4 :
            key2 = intervals.fourth(key, key)
        elif phrase2[0]==5:
            key2 = intervals.fifth(key, key)

    for bars in  phrase1[1][3] :
        for n in bars :
            notes = get_note(n, key1)
            phrase1_list.append(notes)
        
    for bars in phrase2[1][3] :
        for n in bars :
            number_notes+=1
            if get_note(n, key2) in phrase1_list:
                percentage+=1
    
    return (percentage/number_notes)*100


def velocity_phrase(phrase):
    print("phrase : "+str(phrase))
    number_notes = 0
    note_temp = 0
    
    for bars in phrase[3] :
        print(str(bars))
        for note in bars :
            print("note : "+str(note))
            print("temp : "+str(note_temp))
            if note_temp == 0:
                number_notes+=1
            else:
                if note[2]!=note_temp[2]:
                    number_notes+=1
            note_temp = note
    
    if number_notes < 4*phrase[2] :
        return 1 # lent
    
    elif number_notes < 7*phrase[2]  :
        return 2 # moyen
    
    else :
        return 3 # rapide
    