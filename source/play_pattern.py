from mingus.containers.Bar import Bar
from mingus.containers.Note import Note
from mingus.midi import fluidsynth
from pattern_utils import chord_length, get_note_pattern

def play_pattern(pattern, key):
    fluidsynth.init("198_u20_Electric_Grand.SF2") # permet d'initialiser l'instrument

    previews_note = None
    b = Bar(key, (4, 4))
    position_note = 0
    already_used=[]
    for pattern_note in pattern :
        if position_note not in already_used :
            is_chord = chord_length(pattern_note, pattern, position_note)
            if is_chord[2] :
                note_list = []
                # c est un accord
                for p_note in pattern[is_chord[0]:is_chord[1]+1] :
                    note_str = get_note_pattern(p_note, key)
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
                
                b.place_notes(note_list, pattern_note[1])

                        
            else :    
                note_str = get_note_pattern(pattern_note, key)
                note = Note(note_str, pattern_note[5])
                
                if previews_note is not None:
                    if pattern_note[4]=='+':
                        if int(note) < previews_note :
                            note.octave_up()

                    elif pattern_note[4]=='-':
                        if int(note) > previews_note :
                            note.octave_down()
                            
                previews_note = int(note)
                b.place_notes(note, pattern_note[1])
                already_used.append(position_note)
        position_note+=1
            
    fluidsynth.play_Bar(b, 1, 60)                      