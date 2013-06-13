import patterns
from pattern_utils import get_pattern_velocity
from phrase_chooser import *
import random
from note_utils import get_phrase
from right_hand_generator import generate_bar
from transition_utils import *
from mingus.containers.Bar import Bar


def generate_chorus(progression_list, pattern_index, mode, key):
    pattern = patterns.PATTERNS[pattern_index]
    velocity_pattern = get_pattern_velocity(pattern)
    
    phrase_list = []

    list_phrases_4 = choose_chord_4_phrase(mode)
    list_phrases_5 = choose_chord_5_phrase(mode)
    
    if velocity_pattern == 3:
        for phrase in list_phrases_4 :
            if velocity_phrase == 3:
                list_phrases_4.remove(phrase)
                
        for phrase in list_phrases_5 :
            if velocity_phrase == 3:
                list_phrases_5.remove(phrase)

    phrase_4_index = random.randint(0, len(list_phrases_4)-1)

    phrase_4 = list_phrases_4[phrase_4_index]
    phrase_4_chosen = [4, phrase_4]
    phrase_list.append(phrase_4_chosen)
    
    velocity_phrase_4 = velocity_phrase(phrase_4)
    for phrase_5 in list_phrases_5 :
        if abs(velocity_phrase(phrase_5)-velocity_phrase_4)>1 :
            list_phrases_5.remove(phrase_5)
            
            
    compatibility = []
    for phrase_5 in list_phrases_5 :
        phrase_5_to_test = [5, phrase_5]
        compatibility.append(calcul_compatibility(phrase_4_chosen, phrase_5_to_test, key, mode))
    
    list_best_phrase_5 = get_best_options(compatibility)
    index_phrase_5 = random.randint(0, len(list_best_phrase_5)-1)
    
    phrase_5 = list_phrases_5[index_phrase_5]
    phrase_5_chosen = [5, phrase_5]
    phrase_list.append(phrase_5_chosen)

    
    notes_4=[]
    
    chorus = generate_chorus_bars(phrase_list, progression_list, 1, pattern_index, mode, key)
   
    return chorus
    
    # on a les deux phrases du refrain ! 
    # on va generer les bars et la transition


def choose_first_phrases(nb_bars, key, mode, first_chorus_phrase, last_chorus_phrase, pattern_index):
    list_phrases_1 = choose_chord_1_phrase(mode)
    final_list = []
    pattern = patterns.PATTERNS[pattern_index]
    velocity_pattern = get_pattern_velocity(pattern)
    
    if velocity_pattern == 3:
        for phrase in list_phrases_1 :
            if velocity_phrase == 3:
                list_phrases_1.remove(phrase)
                
    phrase_first = choose_best_phrase(list_phrases_1, first_chorus_phrase, key, mode)
    final_list.append(phrase_first)
    phrase_last = choose_best_phrase(list_phrases_1, last_chorus_phrase, key, mode)
    
    for i in range(1, nb_bars-2):
       final_list.append("pouet")
       
    
    final_list.append(phrase_last)
    
    return final_list
    
    
    


def generate_long_right_hand(phrase_list, progression_list, nb_bars, pattern_index, mode, key, chorus):
    return None

def generate_chorus_bars(phrase_list, progression_list, nb_bars, pattern_index, mode='none', key="C"):
    print(str(progression_list))
    chorus = []
    transition = []
    if nb_bars == 1 :
        nb_p = 0
        for progression in progression_list[0] :
            if nb_p%4 == 0 and nb_p>3:
                phrase = get_phrase(progression, phrase_list)
                last_note = None
                nb_bars = 0
                for bars in phrase[1][3] :
                    list_bar = generate_bar(last_note, bars, key, mode, progression, progression_list, nb_p+nb_bars, pattern_index)
                    chorus.append(list_bar)
                    last_note = list_bar[1]
                    nb_bars+=1
                    last_bar = bars

                if phrase[1][1] < 4 and nb_p < 10:
                    # composer le reste TODO en attendant on met du vide
                    last_bar_notes = list_bar[2]

                    next_index = nb_p+4
                    if next_index < 9 :
                        next_progression = progression_list[0][next_index]
                        next_phrase = get_phrase(next_progression, phrase_list)
                        first_bar = next_phrase[1][3][0]
                        first_bar_list = generate_bar(last_note, first_bar, key, mode, next_progression, progression_list, nb_p+4, pattern_index)
                        first_bar_notes = first_bar_list[2]
                        
                        nb_notes_to_generate = get_nb_note_needed(last_bar, first_bar)        
                        
                    #gerer si c'est la fin ! TODO
                        
                    for i in range(4-phrase[1][1]):
                        b = Bar(key, (4,4))
                        b.place_rest(1)
                        transition.append(b)
                nb_p +=1
            else :
                nb_p +=1
                continue
            
    return (chorus, transition)


def choose_best_phrase(list_possible, first_phrase, key, mode):
    
    compatibility = []
    for phrase in list_possible :
        phrase_to_test = [1, phrase]
        compatibility.append(calcul_compatibility(first_phrase, phrase_to_test, key, mode))
    
    list_best_phrase = get_best_options(compatibility)
    index_phrase = random.randint(0, len(list_best_phrase)-1)
    
    phrase = list_possible[index_phrase]
    return [1, phrase]


def choose_between_phrase(list_possible, first_phrase, last_phrase, key, mode):
    compatibility_first = []
    for phrase in list_possible :
        phrase_to_test = [1, phrase]
        compatibility_first.append(calcul_compatibility(first_phrase, phrase_to_test, key, mode))
        
    compatibility_last = []
    for phrase in list_possible :
        phrase_to_test = [1, phrase]
        compatibility_last.append(calcul_compatibility(last_phrase, phrase_to_test, key, mode))
        
        
    while list_possible.length > 1 :
        min_first = min(compatibility_first)
        min_last = min(compatibility_last)
    
