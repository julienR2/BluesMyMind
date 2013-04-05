import mingus.core.notes as notes
import mingus.core.intervals as intervals
#from mingus.midi import fluidsynth
#from mingus.midi import MidiFileOut
from mingus.containers.Bar import Bar
from mingus.containers.Note import Note
from mingus.containers.Track import Track
#import mingus.extra.LilyPond as LilyPond



def progression_to_int(progression):
    num_progression = []
    
    for prog in progression :
        roman = prog.upper()
        nums = ['X', 'V', 'I']
        ints = [10,  5,   1]
        places = []
  
        for i in range(len(roman)):
            c = roman[i]
            value = ints[nums.index(c)]
            # If the next place holds a larger number, this value is negative.
            try:
                nextvalue = ints[nums.index(roman[i +1])]
                if nextvalue > value:
                    value *= -1
            except IndexError:
                # there is no next place.
                pass
            places.append(value)
        sum_roman = 0
        for n in places: 
            sum_roman += n
        num_progression.append(sum_roman)
        
    return num_progression


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

    if pattern[2] == "bemol":
        note = notes.diminish(note)
    elif pattern[2] == "diese" :
        note = notes.augment(note)
    return note


def get_progression_key(note_int, key):
    if note_int == 1 :
        p_key = intervals.unison(key)
    if note_int == 4 :
        p_key = intervals.fourth(key, key)
    if note_int == 5 :
        p_key = intervals.fifth(key, key)
    return p_key
       

def generate_pattern(key = "C", pattern = ((1, 1, "none", '=', 3), (3, 1, "none", '+', 3), (5, 1, "none", '+', 3), (6, 1, "none", '+', 3))):
    progression = ['I', 'I', 'I', 'I', 'IV', 'IV', 'I', 'I', 'V', 'IV', 'I', 'V']
    progression = progression_to_int(progression)
    t = Track()
    #fluidsynth.init("198_u20_Electric_Grand.SF2")

    for p in progression :
        previews_note = None
        p_key = get_progression_key(p, key)
        b = Bar(key, (4, 4))        
        for pattern_note in pattern :
            note_str = get_note_pattern(pattern_note, p_key)
            note = Note(note_str, pattern_note[4])
            if previews_note is not None:
                if pattern_note[3]=='+':
                    if int(note) < previews_note :
                        note.octave_up()
                elif pattern_note[3]=='-':
                    if int(note) > previews_note :
                        note.octave_down()
                        
            previews_note = int(note)
            b + note
        t.add_bar(b)
                    
    #track = LilyPond.from_Track(t)
    #LilyPond.to_png(track, "left_hand")
    #MidiFileOut.write_Track("test_midi.mid", t)
    

            
generate_pattern()
