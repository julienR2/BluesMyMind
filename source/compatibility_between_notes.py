from right_hand import get_note
import mingus.core.intervals as intervals
import mingus.core.notes as notes
from mingus.containers.Note import Note
import mingus.core.notes as notes

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

    note_str = intervals.unison(note.name, note.name)
    print("note_str = "+str(note_str))
    print("note_left = "+str(list_left_note))
    
    if note_str in list_left_note :
        return note
    else :
        while len(list_left_note) != 0 :
            
            print("liste_left_note : "+str(list_left_note))
            note_str = intervals.unison(note.name, note.name)

            for left_note in list_left_note :
                if (intervals.measure(left_note, note_str)>2 and intervals.measure(left_note, note_str)<10) or intervals.measure(left_note, note_str)>11  :
                    print("ecart grand, je supprime : "+str(intervals.measure(left_note, note_str)))
                    list_left_note.remove(left_note)
                else :
                    if note_list[4]=="+":
                        while intervals.measure(left_note, note_str)<3 or (intervals.measure(left_note, note_str)>9 and intervals.measure(left_note, note_str)<12):
                            print("j augmente")
                            note.augment()
                            note_str = intervals.unison(note.name, note.name)
                        list_left_note.remove(left_note)

                    else :
                        while intervals.measure(left_note, note_str)!=0 or intervals.measure(left_note, note_str)>9 :
                            print("je diminue")
                            note.diminish()
                            note_str = intervals.unison(note.name, note.name)
                        list_left_note.remove(left_note)


    print("returned note : "+str(note))
                            
    return note

def change_note_if_needed(time, note, pattern_index, progression, note_list, key):
    
    if progression == 'IV' :
            key = intervals.fourth(key, key)
    elif progression == 'V' :
            key = intervals.fifth(key, key)
            
    list_left = get_note_list_left_hand(pattern_index, key, time)
    new_note = get_best_note(note, list_left, note_list)
    
    return new_note
    
        

