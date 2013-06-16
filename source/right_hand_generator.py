from compatibility_between_notes import change_note_if_needed
from end_generator import generate_end_bars
from mingus.containers.Bar import Bar
from mingus.containers.Note import Note
from mingus.containers.Track import Track
from note_utils import get_note, get_phrase
from pattern_utils import chord_length
from source.transition_utils import generate_transition
from transition_utils import get_nb_note_needed
import mingus.core.intervals as intervals


def use_phrase(phrase_list, progression_list, nb_bars, pattern_index, mode='none', key="C"):
    print(str(progression_list))
    t = Track()
    if nb_bars == 1 :
        nb_p = 0
        for progression in progression_list[0] :
            if nb_p%4 == 0 :
                phrase = get_phrase(progression, phrase_list)
                last_note = None
                nb_bars = 0
                for bars in phrase[1][3] :
                    list_bar = generate_bar(last_note, bars, key, mode, progression, progression_list, nb_p+nb_bars, pattern_index)
                    b = list_bar[0]
                    last_note = list_bar[1]
                    nb_bars+=1
                    t.add_bar(b)
                    last_bar = bars

                if phrase[1][1] < 4 :
                    # composer le reste TODO en attendant on met du vide
                    last_bar_notes = list_bar[2]
                    print("lala "+str(last_bar_notes))

                    next_index = nb_p+4
                    if next_index < 9 :
                        next_progression = progression_list[0][next_index]
                        next_phrase = get_phrase(next_progression, phrase_list)
                        first_bar = next_phrase[1][3][0]
                        first_bar_list = generate_bar(last_note, first_bar, key, mode, next_progression, progression_list, nb_p+4, pattern_index)
                        first_bar_notes = first_bar_list[2]
                        
                        nb_notes_to_generate = get_nb_note_needed(last_bar, first_bar)
                        
                        print "****************** je vais generer la transition ! ****************"
                        transition_bar = generate_transition(first_bar_notes, last_bar_notes, nb_notes_to_generate, pattern_index, key)
                        print "***************************** Fini ! ******************************"
                                                
                        for i in range(len(transition_bar)):
                            t.add_bar(transition_bar[i])
                    else :
                        list_end = generate_end_bars(bars, list_bar[2], pattern_index, key, mode)
                        for end_bar in list_end :
                            t.add_bar(end_bar)
                        
                        break
                    
                nb_p +=1
            else :
                nb_p +=1
                continue
        return t
                    


            
def generate_bar(previews_note, bar, key, mode, progression, progression_list, nb_p, pattern_index):
    if mode == 'mixolydien' :
        if progression == 'IV' :
            key = intervals.fourth(key, key)
        elif progression == 'V' :
            key = intervals.fifth(key, key)
        
    b = Bar(key, (4, 4))
    position_note = 0
    already_used=[]
    list_note = []
    
    for bar_note in bar :
        if position_note not in already_used :
            is_chord = chord_length(bar_note, bar, position_note)
            if is_chord[2] :
                note_list = []
                # c est un accord
                for p_note in bar[is_chord[0]:is_chord[1]+1] :
                    note_str = get_note(p_note, key)
                    note = Note(note_str, p_note[5])
                    if previews_note is not None:
                        if p_note[4]=='+':
                            if int(note) < previews_note :
                                note.octave_up()
                        elif p_note[4]=='-':
                            if int(note) > previews_note :
                                note.octave_down()
                    current_progression = progression_list[0][nb_p]
                    note = change_note_if_needed(bar_note[2], note, pattern_index, current_progression, bar_note, key)     
                    previews_note = int(note)
                    
                    #appeler best_note la aussi
                    note_list.append(note)
                    list_note.append(note)
                    
                for n in range(is_chord[0], is_chord[1]+1):
                    already_used.append(n)
                
                b.place_notes(note_list, bar_note[1])

                        
            else :  
                note_str = get_note(bar_note, key)
                note = Note(note_str, bar_note[5])
                
                if previews_note is not None:
                    if bar_note[4]=='+':
                        if int(note) < previews_note :
                            note.octave_up()

                    elif bar_note[4]=='-':
                        if int(note) > previews_note :
                            note.octave_down()
                
                # la un faut appeler le truc pour modifier la note
                current_progression = progression_list[0][nb_p]
                note = change_note_if_needed(bar_note[2], note, pattern_index, current_progression, bar_note, key)
                            
                previews_note = int(note)
                list_note.append(note)
                b.place_notes(note, bar_note[1])
                already_used.append(position_note)
        position_note+=1
     
    return (b, previews_note, list_note)
            
