from mingus.containers import Composition
from mingus.midi import MidiFileOut, fluidsynth
from generate_pattern import generate_pattern 
from choose_progression import on_progression_type_change
from right_hand import choose_phrases



def generate_composition(pattern, progression_type, nb_bars, mode='none', key="C", rythm=60):
    fluidsynth.init("198_u20_Electric_Grand.SF2") # permet d'initialiser l'instrument
    newComposition = Composition()
    progression_list = on_progression_type_change(progression_type, nb_bars)
    left_hand = generate_pattern(progression_list, key, pattern, nb_bars)
    newComposition.add_track(left_hand)
    MidiFileOut.write_Composition("myComposition.mid", newComposition, rythm, False)
    # truc pour la main droite
    list_phrase = choose_phrases(key, mode, nb_bars)
    print(str(list_phrase))

generate_composition(((1, 8, 1, "none", '=', 2), (5, 8, 1, "none", '+', 2), (1, 8, 1.5, "none", '=', 2), (5, 8, 1.5, "none", '+', 2), (2, 8, 2, "diese", '=', 2), (3, 8, 2.5, "none", '+', 2), (1, 8, 3, "none", '=', 2), (5, 8, 3, "none", '+', 2), (1, 8, 3.5, "none", '=', 2), (5, 8, 3.5, "none", '+', 2), (2, 8, 4, "diese", '=', 2), (3, 8, 4.5, "none", '+', 2)), 12, 1, 'none', "D", 60)    


