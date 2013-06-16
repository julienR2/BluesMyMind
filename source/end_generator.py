from pattern_utils import get_pattern_velocity
from compatibility_between_notes import get_note_list_left_hand
import mingus.core.intervals as intervals
from mingus.containers.Bar import Bar
from mingus.containers.Note import Note

import random
import mingus.core.chords as chords

def get_nb_notes(last_bar):
    velocity = get_pattern_velocity(last_bar)

    if velocity == 1 :
        return [len(last_bar), 1]
    elif velocity == 2:
        return [4, 2]
    else :
        return [6, 3]
    
    

def get_compatible_notes(pattern_index, right_hand_list, key, time):
    left_hand_list = get_note_list_left_hand(pattern_index, key, time)
    list_notes = []
    if len(left_hand_list)==0 :
        return right_hand_list
    
    for left_note in left_hand_list :
        for right_note in right_hand_list :
            note_str = intervals.unison(right_note.name, right_note.name)   
            if (intervals.measure(left_note, note_str)>2 and intervals.measure(left_note, note_str)<10) or intervals.measure(left_note, note_str)>11  :
                list_notes.append(right_note)
    return list_notes


def get_max_length_note(bar, nb_notes_left):
    test_bar = bar
    length_list = []
    
    for l in [1, 2, 4, 6, 8]:
        
        if test_bar.place_notes("C-4", l) :  
 
            current = test_bar.current_beat
            length = test_bar.length
            rest = length - current
            
            if nb_notes_left - 1 > 0 and rest > 0:
                possible = (nb_notes_left-1) / rest

                
                if possible <= 8 :
                    length_list.append(l)
            
            elif nb_notes_left-1 == 0 :
                length_list.append(l)
                test_bar.remove_last_entry()
                break
            
            test_bar.remove_last_entry()
    
    return length_list  


def get_best_notes(list_compatible, last_note):  
    #last_note[2] = nom
    #last_note[1] = longueur
    final_list = []
    
    for note in list_compatible :
        if abs(int(last_note) - int(note)) < 7 :
            final_list.append(note)
    
    if len(final_list) == 0 :
        for note in list_compatible :
            if abs(int(last_note) - int(note)) < 14 :
                final_list.append(note)
        
    return final_list
    
def generate_end_bars(previews_bar, previews_bar_notes, pattern_index, key, mode):
    # on genere deux mesures de fin
    # previews_bar = format de la bdd
    nb_notes = get_nb_notes(previews_bar)
    print("nb_notes : "+str(nb_notes))
    first_bar = Bar()
    last_bar = Bar()
    print("previews_bar_notes : "+ str(previews_bar_notes))
    last_index = len(previews_bar_notes)-1
    last_note = previews_bar_notes[last_index]
    """while last_note is None :
        if previews_bar_notes[last_index][2] is not None :
            last_note = previews_bar_notes[last_index]
        else :
            last_index -=  1"""
    
    for i in range(1, nb_notes[0]):
        time = first_bar.current_beat + 1
        list_compatible = get_compatible_notes(pattern_index, previews_bar_notes, key, time)
        list_length = get_max_length_note(first_bar, nb_notes[0]-i)
        best_notes = get_best_notes(list_compatible, last_note)
        chosen_note = best_notes[random.randint(0, len(best_notes)-1)]
        chosen_length = list_length[random.randint(0, len(list_length)-1)]
        first_bar.place_notes(chosen_note.name, chosen_length)
        
    for i in range(1, nb_notes[1]):
        time = last_bar.current_beat + 1
        list_compatible = get_compatible_notes(pattern_index, previews_bar_notes, key, time)
        list_length = get_max_length_note(last_bar, nb_notes[1]-i)
        best_notes = get_best_notes(list_compatible, last_note)
        chosen_note = best_notes[random.randint(0, len(best_notes)-1)]
        chosen_length = list_length[random.randint(0, len(list_length)-1)]
        #chosen_note.octave
        if mode == "mixolydien" :
            chord = chords.seventh(chosen_note.name, key)
            chord_list = []
            for note in chord :
                note_m = Note(note, chosen_note.octave)
                chord_list.append(note_m)
            last_bar.place_notes(chord_list, chosen_length)
        else :
            chord = chords.triad(chosen_note.name, key)
            chord_list = []
            for note in chord :
                note_m = Note(note, chosen_note.octave)
                chord_list.append(note_m)
            last_bar.place_notes(chord_list, chosen_length)
            
        return [first_bar, last_bar]
        
        
        
    
        
        
       