from right_hand import get_note
import mingus.core.intervals as intervals
import mingus.core.notes as notes
from mingus.containers.Note import Note

import patterns


def get_note_list_left_hand(pattern_index, key, time):
    
    pattern = patterns.PATTERNS[pattern_index]
    list_note = []
    for note in pattern :
        if note[2]==time :
            note_str = get_note(note, key)
            list_note.append(note_str)
    
    return list_note


def get_note_list_right_hand(bar, key, time):
    list_note = []
    for note in bar :
        if note[2]==time :
            list_note.append(get_note(note, key))
    return list_note

def get_best_note(note , list_left_note, note_list):
    modif = True
    note_str = intervals.unison(note.name, note.name)
    
    if note_str in list_left_note :
        return note
    else :
        while modif :
            nb_modif = 0
            note_str = intervals.unison(note.name, note.name)
            for left_note in list_left_note :    
                if (intervals.measure(left_note, note_str)>2 and intervals.measure(left_note, note_str)<10) or intervals.measure(left_note, note_str)>11  :
                    print("note valide")
                
                elif intervals.measure(left_note, note_str) < 3 :
                    if note_list[4]=="+":
                        while intervals.measure(left_note, note_str) < 3 :
                                note.augment()
                                note_str = intervals.unison(note.name, note.name)  
                                nb_modif +=1   
                    elif note_list[4]=="-":
                        while intervals.measure(left_note, note_str)!=0 :
                                note.diminish()
                                note_str = intervals.unison(note.name, note.name)
                                nb_modif +=1
                    else : 
                        note.augment()
                        note_str = intervals.unison(note.name, note.name)  
                        nb_modif +=1   
                
                else :
                    if note_list[4]=="+":
                        while intervals.measure(note_str, left_note) < 3 :
                            note.augment()
                            note_str = intervals.unison(note.name, note.name)  
                            nb_modif +=1    
                    elif note_list[4]=="-":
                        while intervals.measure(note_str, left_note) != 0 :
                            note.diminish()
                            note_str = intervals.unison(note.name, note.name)   
                            nb_modif +=1  
                    
                    elif intervals.measure(left_note, note_str)>9: 
                        note.augment()
                        note_str = intervals.unison(note.name, note.name)  
                        nb_modif +=1 
                 
            if nb_modif == 0 :
                modif = False
                 
                            
    return note

def change_note_if_needed(time, note, pattern_index, progression, note_list, key):
    
    if progression == 'IV' :
            key = intervals.fourth(key, key)
    elif progression == 'V' :
            key = intervals.fifth(key, key)
            
    list_left = get_note_list_left_hand(pattern_index, key, time)
    new_note = get_best_note(note, list_left, note_list)
    
    return new_note
    
        

