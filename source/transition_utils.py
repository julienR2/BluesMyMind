from generate_blues_scale import generate_blues_scale
from mingus.containers.Bar import Bar
from mingus.containers.Note import Note
import phrases
from end_generator import get_compatible_notes, get_max_length_note, get_best_notes
import random

def get_nb_note_needed(last_bar, first_bar):
    nb_last = nb_note_bar(last_bar)
    nb_first = nb_note_bar(first_bar)
    dif = abs(nb_last - nb_first)
    
    if dif < 3 :
        return [nb_last, nb_first]

    else :
        if nb_last > nb_first :
            return [nb_last - (dif/2), nb_first + (dif/2)]
        else :
            return [nb_last + (dif/2), nb_first - (dif/2)]
    


def nb_note_bar(bar):
    number_notes = 0
    note_temp = 0
    for note in bar :
        if note_temp == 0:
            number_notes+=1
        else:
            if note[2]!=note_temp[2]:
                number_notes+=1
        note_temp = note
        
    return number_notes

def get_list_notes(last_bar, first_bar):
    return None

def generate_transition(previous_phrase, next_phrase, nb_note_needed, pattern_index, key):
    
    previous_note = Note(previous_phrase[len(previous_phrase)-1])
    next_note = Note(next_phrase[0])
    selected_notes = get_note_between(previous_note, next_note, previous_phrase)
    temp_selected = get_note_between(previous_note, next_note, next_phrase)
    
    for i in range(len(temp_selected)):
        if temp_selected[i] not in selected_notes:
            selected_notes.append(temp_selected[i])
            
    if (float(len(selected_notes))/abs((nb_note_needed[0]+nb_note_needed[1])))<(float(3)/4):
        temp_from_scale = get_note_between(previous_note, next_note, generate_blues_scale(key))
        for i in range(len(temp_from_scale)):
            if temp_from_scale[i] not in selected_notes:
                selected_notes.append(temp_from_scale[i])
    
    first_bar = Bar()
    last_bar = Bar()
    
    for i in range(1, nb_note_needed[0]):
        time = first_bar.current_beat + 1
        list_compatible = get_compatible_notes(pattern_index, selected_notes, key, time)
        print "liste compatible : " + str(list_compatible) 
        list_length = get_max_length_note(first_bar, nb_note_needed[0]-i)
        best_notes = get_best_notes_transition(list_compatible, previous_note, next_note, 0,  float(i)/nb_note_needed[0])
        print "best_notes : " + str(best_notes)
        chosen_note = best_notes[random.randint(0, len(best_notes)-1)]
        chosen_length = list_length[random.randint(0, len(list_length)-1)]
        first_bar.place_notes(chosen_note.name, chosen_length)
        
    for i in range(1, nb_note_needed[1]):
        time = last_bar.current_beat + 1
        list_compatible = get_compatible_notes(pattern_index, selected_notes, key, time)
        list_length = get_max_length_note(last_bar, nb_note_needed[1]-i)
        best_notes = get_best_notes_transition(list_compatible, previous_note, next_note, 1, float(i)/nb_note_needed[1])
        chosen_note = best_notes[random.randint(0, len(best_notes)-1)]
        chosen_length = list_length[random.randint(0, len(list_length)-1)]
        last_bar.place_notes(chosen_note.name, chosen_length)
    
    if last_bar.length - last_bar.current_beat != 0 : 
        print("ajout de silence")
        space_left = 1.0 / (last_bar.length - last_bar.current_beat)
        last_bar.place_rest(space_left) 
    
    if first_bar.length - first_bar.current_beat != 0 : 
        print("ajout de silence")
        space_left = 1.0 / (first_bar.length - first_bar.current_beat)
        first_bar.place_rest(space_left)         
    
    
        
    return [first_bar, last_bar]
        
def get_best_notes_transition(list_note, previous_note, next_note, bar, percent): 
    final_list = []
    
    if (bar == 0):
        if (percent<(float(75)/100)): 
            for note in list_note :
                if (abs(int(previous_note) - int(note)) < 7):
                    final_list.append(note)
        else:
            for note in list_note :
                if (abs(int(previous_note) - int(note)) < 7) and (abs(int(next_note) - int(note)) < 7):
                    final_list.append(note)
    elif (bar==1):
        if (percent<(float(25)/100)): 
            for note in list_note :
                if (abs(int(previous_note) - int(note)) < 7) and (abs(int(next_note) - int(note)) < 7):
                    final_list.append(note)
        else:
            for note in list_note :
                if (abs(int(next_note) - int(note)) < 7):
                    final_list.append(note)
    
    if len(final_list) == 0 :
        if (bar == 0):
            if (percent<(float(75)/100)): 
                for note in list_note :
                    if (abs(int(previous_note) - int(note)) < 14):
                        final_list.append(note)
            else:
                for note in list_note :
                    if (abs(int(previous_note) - int(note)) < 14) and (abs(int(next_note) - int(note)) < 14):
                        final_list.append(note)
        elif (bar==1):
            if (percent<(float(25)/100)): 
                for note in list_note :
                    if (abs(int(previous_note) - int(note)) < 14) and (abs(int(next_note) - int(note)) < 14):
                        final_list.append(note)
            else:
                for note in list_note :
                    if (abs(int(next_note) - int(note)) < 14):
                        final_list.append(note)
        
    return final_list
        
def get_note_between(previous_note, next_note, liste_note):
    selected_notes= []
    if previous_note < next_note:
        if int(next_note)-int(previous_note)<3:
            min = Note(previous_note)
            max = Note(next_note)
            for i in range(2):
                min.diminish()    
                max.augment()
        else:
            min = Note(previous_note)
            max = Note(next_note)
    elif previous_note > next_note:
        if int(previous_note)-int(next_note)<3:
            min = Note(next_note)
            max = Note(previous_note)
            for i in range(2):
                min.diminish()    
                max.augment()
        else:
            min = Note(next_note)
            max = Note(previous_note)
    elif previous_note == next_note:
        min = Note(next_note)
        max = Note(previous_note)
        for i in range(4):
            min.diminish()    
            max.augment()
    
    for i in range(len(liste_note)):
        current = Note(liste_note[i])
        if current not in selected_notes:
            if min<=current and current<=max:
                selected_notes.append(current)
    return selected_notes