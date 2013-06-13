import mingus.core.notes as notes
import mingus.core.intervals as intervals


def get_note_pattern(pattern, key):
    if pattern[0] == 1 :
        note = intervals.unison(key)
    elif pattern[0] == 2 :
        note = intervals.second(key, key)
    elif pattern[0] == 3 :
        note = intervals.third(key, key)
    elif pattern[0] == 4 :
        note = intervals.fourth(key, key)
    elif pattern[0] == 5 :
        note = intervals.fifth(key, key)
    elif pattern[0] == 6 :
        note = intervals.sixth(key, key)
    elif pattern[0] == 7 :
        note = intervals.seventh(key, key)

    if pattern[3] == "bemol":
        note = notes.diminish(note)
    elif pattern[3] == "diese" :
        note = notes.augment(note)
    return note

    

def chord_length(pattern_note, pattern, position_note):
    begin = position_note
    end = position_note
    chord = False
    if len(pattern) > 1 :
        for p_note in pattern[position_note+1:] :
            if p_note[2] == pattern_note[2] :
                chord = True
                end+=1
            else :
                break      
    return (begin, end, chord)

def get_pattern_velocity(pattern):
    number_notes = 0
    note_temp = 0
    if len(pattern) < 2:
        return 1
    else :
        for note in pattern :
    
            if note_temp == 0:
                number_notes+=1
            else:
                if note[2]!=note_temp[2]:
                    number_notes+=1
            note_temp = note
        
        if number_notes < 4:
            return 1 # lent
        
        elif number_notes < 7 :
            return 2 # moyen
        
        else :
            return 3 # rapide
        
