from mingus.containers import Composition
from mingus.midi import MidiFileOut, fluidsynth
from generate_pattern import generate_pattern 
from choose_progression import on_progression_type_change
from right_hand import choose_phrases
from right_hand_generator import use_phrase


def generate_composition(pattern_index, progression_type, nb_bars, mode='none', key="C", rythm=60):
    fluidsynth.init("198_u20_Electric_Grand.SF2") # permet d'initialiser l'instrument
    newComposition = Composition()
    progression_list = on_progression_type_change(progression_type, nb_bars)
    
     # truc pour la main droite
    phrase_list = choose_phrases(key, mode, nb_bars)
    right_hand = use_phrase(phrase_list, progression_list, nb_bars, mode='none', key="C")
    newComposition.add_track(right_hand)
    
    left_hand = generate_pattern(progression_list, key, pattern_index, nb_bars)
    newComposition.add_track(left_hand)
    MidiFileOut.write_Composition("myCompo.mid", newComposition, rythm, False)
   
    return newComposition

def save_as_midi(name, composition, rythm):
    MidiFileOut.write_Composition(name+".mid", composition, rythm, False)

#TODO save_as_pdf


