from mingus.containers.Bar import Bar
from mingus.containers.Note import Note
from mingus.containers.Track import Track
from pattern_utils import chord_length, get_note_pattern
from progression_utils import get_progression_key, progression_to_int
import patterns
import mingus.core.intervals as intervals
import mingus.core.notes as notes
import mingus.extra.LilyPond as LilyPond #decommenter pour tester lilypond : > pdf



def generate_pattern(progression_list, key = "C", pattern_index = 0, nb_bars=1):
    pattern = patterns.PATTERNS[pattern_index]
    t = Track()
    for progression in progression_list:
        progression = progression_to_int(progression)
        for p in progression : # permet d'avancer dans la progression des mesures
            previews_note = None
            p_key = get_progression_key(p, key)
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
                            note_str = get_note_pattern(p_note, p_key)
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
                        note_str = get_note_pattern(pattern_note, p_key)
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
                
            t.add_bar(b)

    return t
    #decommander les trois lignes precedentes pour tester si lilypond et fluidsynth marche (pdf et midi)

            
