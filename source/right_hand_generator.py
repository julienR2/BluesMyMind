from mingus.containers.Track import Track
from mingus.containers.Bar import Bar
from pattern_utils import chord_length
from mingus.containers.Note import Note
from right_hand import get_note
import mingus.core.intervals as intervals


def use_phrase(phrase_list, progression_list, nb_bars, mode='none', key="C"):
    print(str(progression_list))
    t = Track()
    if nb_bars == 1 :
        nb_p = 0
        for progression in progression_list[0] :
            if nb_p%4 == 0 :
                phrase = get_phrase(progression, phrase_list)
                last_note = None
                for bars in phrase[1][3] :
                    print(str(bars))
                    list_bar = generate_bar(last_note, bars, key, mode, progression)
                    b = list_bar[0]
                    last_note = list_bar[1]
                    t.add_bar(b)

                if phrase[1][1] < 4 :
                    # composer le reste TODO en attendant on met du vide
                    for i in range(4-phrase[1][1]):
                        b = Bar(key, (4,4))
                        b.place_rest(1)
                        t.add_bar(b)
                nb_p +=1
            else :
                nb_p +=1
                continue
        return t
                    

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
            
def generate_bar(previews_note, bar, key, mode, progression):
    if mode == 'mixolydien' :
        if progression == 'IV' :
            key = intervals.fourth(key, key)
        elif progression == 'V' :
            key = intervals.fifth(key, key)
        
    b = Bar(key, (4, 4))
    position_note = 0
    already_used=[]
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
                    previews_note = int(note)
                    note_list.append(note)
                    
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
                            
                previews_note = int(note)
                b.place_notes(note, bar_note[1])
                already_used.append(position_note)
        position_note+=1
     
    return (b, previews_note)
            