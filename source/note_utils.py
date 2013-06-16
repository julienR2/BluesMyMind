import mingus.core.intervals as intervals
import mingus.core.notes as notes


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

def get_phrase(progression, phrase_list):
    for phrase in phrase_list : 
        if progression == 'I' :
            if phrase[0] == 1 :
                return phrase
            
        elif progression == 'IV' :
            if phrase[0] == 4 :
                return phrase
        
        elif progression == 'V' :
            if phrase[0] == 5 :
                return phrase
            
#pour une note au format liste    
def augmente_note (note, hauteur):
    if note[0] + hauteur > 7:
        return ((note[0]+hauteur)%7, note[1], note[2], note[3], note[4], note[5]+1)
    else:
        return (note[0]+hauteur, note[1], note[2], note[3], note[4], note[5])

#pour une note au format liste
def diminue_note(note, hauteur):
    if note[0] - hauteur < 1:
        return (7-abs(note[0]-hauteur), note[1], note[2], note[3], note[4], note[5]-1)
    else:
        return (note[0]-hauteur, note[1], note[2], note[3], note[4], note[5])